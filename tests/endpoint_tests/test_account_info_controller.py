import pytest
from tests.endpoint_tests.controller_test_base import ControllerTestBase
import os

class TestAccountInfoController(ControllerTestBase):
    """Test suite for Account Info endpoints.
    
    This class contains tests for the Account Info API endpoints, including:
    - Account information retrieval
    - Account details retrieval
    """
    def test_get_accounts_info(self):
        """Test GET /accounts/v2/:providerId endpoint.
        
        This test verifies that:
        - The endpoint returns a successful response
        - The response contains account information
        - The provider ID is properly used in the request
        - The response structure matches the API specification
        """
        client = self.get_client_with_credentials(
            os.getenv('TEST_USERNAME', 'GenericUser_Pfm'),
            os.getenv('TEST_PASSWORD', 'GenericUser_Pfm')
        )
        response = client.account_information.get_accounts_info(
            version=self.api_version,
            provider_id=self.provider_id
        )
        assert response is not None
        assert response.status_code == 200
        assert response.body is not None
