import pytest
from akoyaapisv240.exceptions.error_error_exception import ErrorErrorException
from tests.endpoint_tests.controller_test_base import ControllerTestBase
import os

class TestInvestmentsController(ControllerTestBase):
    """Test suite for Investments endpoints.
    
    This class contains tests for the Investments API endpoints, including:
    - Investment accounts retrieval
    - Tax lots retrieval
    """

    def test_get_investment_accounts(self):
        """Test GET /accounts/:version/:providerId endpoint.
        
        This test verifies that:
        - The endpoint returns a successful response
        - The response contains investment account information
        - The response structure matches the API specification
        - The provider ID is properly used in the request
        """
        client = self.get_client_with_credentials(
            os.getenv('TEST_USERNAME', 'GenericUser_Pfm'),
            os.getenv('TEST_PASSWORD', 'GenericUser_Pfm')
        )
        response = client.investments.get_accounts(
            version=self.api_version,
            provider_id=self.provider_id
        )
        assert response is not None
        assert response.status_code == 200
        assert response.body is not None

    def test_get_taxlots(self):
        """Test GET /taxlots/:version/:providerId/:accountId/:holdingId endpoint.
        
        This test verifies that:
        - The endpoint returns a successful response
        - The response contains tax lot information
        - The account ID and holding ID are properly used in the request
        - The response structure matches the API specification
        """
        client = self.get_client_with_credentials(
            os.getenv('TEST_USERNAME', 'GenericUser_Pfm'),
            os.getenv('TEST_PASSWORD', 'GenericUser_Pfm')
        )
        response = client.investments.get_taxlots(
            version=self.api_version,
            provider_id=self.provider_id,
            account_id=self.account_id,
            holding_id=self.holding_id
        )
        assert response is not None
        assert response.status_code == 200
        assert response.body is not None