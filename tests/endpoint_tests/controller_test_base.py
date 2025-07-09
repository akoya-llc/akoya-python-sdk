import os
import pytest
from dotenv import load_dotenv
from akoyaapisv240.configuration import Configuration, Environment
from akoyaapisv240.akoyaapisv_240_client import Akoyaapisv240Client
from akoyaapisv240.http.auth.oauth_2 import AuthorizationCodeAuthCredentials
import logging
from akoyaapisv240.logging.configuration.api_logging_configuration import LoggingConfiguration
from akoyaapisv240.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from akoyaapisv240.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration
# Load environment variables
load_dotenv()

class ControllerTestBase:
    def setup_method(self):
        """Set up test method by reading environment variables."""
        self.api_version = os.environ.get("AKOYA_API_VERSION")
        self.provider_id = os.environ.get("AKOYA_PROVIDER_ID")
        self.statement_account_id = os.environ.get("STATEMENT_ACCOUNT_ID")
        self.account_id = os.environ.get("TAXLOT_ACCOUNT_ID")
        self.holding_id = os.environ.get("HOLDING_ID")
        self.statement_id = os.environ.get("STATEMENT_ID")
        
    def get_client_with_credentials(self, username, password):
        """
        Initialize the Akoyaapisv240Client using the provided username and password for the consent flow.
        """
        env = os.getenv('ENVIRONMENT')
        environment = Environment.SANDBOX if env == 'SANDBOX' else Environment.PRODUCTION

        client = Akoyaapisv240Client(
            authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
                oauth_client_id=os.getenv('OAUTH_CLIENT_ID'),
                oauth_client_secret=os.getenv('OAUTH_CLIENT_SECRET'),
                oauth_redirect_uri=os.getenv('OAUTH_REDIRECT_URI')
            ),
            environment=environment
        )

        auth_url = client.acg_auth.get_authorization_url(
            connector=os.getenv('CONNECTOR'),
            state=os.getenv('STATE')
        )

        # Use provided credentials for consent flow
        code = self._run_consent_flow_with_credentials(auth_url, username, password)

        token = client.acg_auth.fetch_token(code)
        if not token:
            raise Exception("Failed to obtain OAuth token")
        authorization_code_auth_credentials = client.config.authorization_code_auth_credentials.clone_with(oauth_token=token)
        config = client.config.clone_with(authorization_code_auth_credentials=authorization_code_auth_credentials)
        client = Akoyaapisv240Client(config=config)
        self.config = config
        return client

    def _run_consent_flow_with_credentials(self, auth_url, username, password):
        """
        Run the consent flow using Playwright with specific credentials and return the authorization code
        """
        from playwright.sync_api import sync_playwright

        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            try:
                # Navigate to auth URL
                page.goto(auth_url)

                # Login
                page.locator("input[type=\"text\"]").click()
                page.locator("input[type=\"text\"]").fill(username)
                page.locator("input[type=\"password\"]").click()
                page.locator("input[type=\"password\"]").fill(password)
                page.get_by_role("button", name="Sign in →").click()

                # Click Next
                page.get_by_role("button", name="Next").click()

                # Check all account checkboxes
                checkboxes = page.locator('input[type="checkbox"][name="account"]')
                for checkbox in checkboxes.all():
                    checkbox.check(force=True)

                # Click Approve
                page.get_by_role("button", name="Approve").click()

                # Wait for redirect and extract code
                page.wait_for_url(f"{os.getenv('RETURN_URL')}*")
                url = page.url
                code = url.split('code=')[1].split('&')[0]
                return code

            except Exception as e:
                page.screenshot(path="consent_flow_failure.png")
                raise e
            finally:
                context.close()
                browser.close() 