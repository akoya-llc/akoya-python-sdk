import os
import pytest
from dotenv import load_dotenv
from akoyaapisv240.configuration import Configuration, Environment
from akoyaapisv240.akoyaapisv_240_client import Akoyaapisv240Client
from akoyaapisv240.http.auth.oauth_2 import AuthorizationCodeAuthCredentials
from akoyaapisv240.exceptions.api_exception import ApiException
from akoyaapisv240.api_helper import APIHelper
from tests.endpoint_tests.controller_test_base import ControllerTestBase

# Load environment variables
load_dotenv()

class TestErrorScenarios(ControllerTestBase):

    @pytest.fixture(scope="class")
    def client_for_error_scenario(self):
        return self._get_client_for_error_scenario

    def _get_client_for_error_scenario(self, username, password):
        # Get environment from env var, default to SANDBOX
        env = os.getenv('ENVIRONMENT')
        environment = Environment.SANDBOX if env == 'SANDBOX' else Environment.PRODUCTION

        # Initialize client with Authorization Code credentials (without token)
        client = Akoyaapisv240Client(
            authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
                oauth_client_id=os.getenv('OAUTH_CLIENT_ID'),
                oauth_client_secret=os.getenv('OAUTH_CLIENT_SECRET'),
                oauth_redirect_uri=os.getenv('OAUTH_REDIRECT_URI')
            ),
            environment=environment
        )

        # Get authorization URL
        auth_url = client.acg_auth.get_authorization_url(
            connector=os.getenv('CONNECTOR'),
            state=os.getenv('STATE')
        )

        # Run consent flow to get authorization code
        code = self._run_consent_flow_with_credentials(auth_url, username, password)

        # Get token using the code
        token = client.acg_auth.fetch_token(code)
        if not token:
            raise Exception("Failed to obtain OAuth token")
        # Update client with authorization code credentials (with token)
        authorization_code_auth_credentials = client.config.authorization_code_auth_credentials.clone_with(oauth_token=token)
        config = client.config.clone_with(authorization_code_auth_credentials=authorization_code_auth_credentials)
        client = Akoyaapisv240Client(config=config)

        # Save config for other tests
        self.config = config

        return client

    def test_mikomo_500_internal_server_error(self):
        try:
            client = self._get_client_for_error_scenario("mikomo_500", "mikomo_500")
            # Make any API call to trigger the error
            client.account_information.get_accounts_info(version=self.api_version, provider_id=self.provider_id)
            pytest.fail("APIException was not raised")
        except ApiException as e:
            error_response = APIHelper.json_deserialize(e.response.text)
            assert error_response["code"] == 500

    def test_mikomo_501_subsystem_unavailable(self):
        try:
            client = self._get_client_for_error_scenario("mikomo_501", "mikomo_501")
            client.account_information.get_accounts_info(version=self.api_version, provider_id=self.provider_id)
            pytest.fail("APIException was not raised")
        except ApiException as e:
            error_response = APIHelper.json_deserialize(e.response.text)
            assert error_response["code"] == 501

    def test_mikomo_601_customer_not_found(self):
        try:
            client = self._get_client_for_error_scenario("mikomo_601", "mikomo_601")
            client.account_information.get_accounts_info(version=self.api_version, provider_id=self.provider_id)
            pytest.fail("APIException was not raised")
        except ApiException as e:
            error_response = APIHelper.json_deserialize(e.response.text)
            assert error_response["code"] == 601

    def test_mikomo_602_customer_not_authorized(self):
        try:
            client = self._get_client_for_error_scenario("mikomo_602", "mikomo_602")
            client.account_information.get_accounts_info(version=self.api_version, provider_id=self.provider_id)
            pytest.fail("APIException was not raised")
        except ApiException as e:
            error_response = APIHelper.json_deserialize(e.response.text)
            assert error_response["code"] == 602

    def test_mikomo_701_account_not_found(self):
        try:
            client = self._get_client_for_error_scenario("mikomo_701", "mikomo_701")
            client.account_information.get_accounts_info(version=self.api_version, provider_id=self.provider_id)
            pytest.fail("APIException was not raised")
        except ApiException as e:
            error_response = APIHelper.json_deserialize(e.response.text)
            assert error_response["code"] == 701

    def test_mikomo_702_invalid_start_or_end_date(self):
        try:
            client = self._get_client_for_error_scenario("mikomo_702", "mikomo_702")
            client.account_information.get_accounts_info(version=self.api_version, provider_id=self.provider_id)
            pytest.fail("APIException was not raised")
        except ApiException as e:
            error_response = APIHelper.json_deserialize(e.response.text)
            assert error_response["code"] == 702

    def test_mikomo_703_invalid_date_range(self):
        try:
            client = self._get_client_for_error_scenario("mikomo_703", "mikomo_703")
            client.account_information.get_accounts_info(version=self.api_version, provider_id=self.provider_id)
            pytest.fail("APIException was not raised")
        except ApiException as e:
            error_response = APIHelper.json_deserialize(e.response.text)
            assert error_response["code"] == 703

    def test_mikomo_704_account_type_not_supported(self):
        try:
            client = self._get_client_for_error_scenario("mikomo_704", "mikomo_704")
            client.account_information.get_accounts_info(version=self.api_version, provider_id=self.provider_id)
            pytest.fail("APIException was not raised")
        except ApiException as e:
            error_response = APIHelper.json_deserialize(e.response.text)
            assert error_response["code"] == 704
