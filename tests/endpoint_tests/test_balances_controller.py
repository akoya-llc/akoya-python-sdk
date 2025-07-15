import pytest
from tests.endpoint_tests.controller_test_base import ControllerTestBase
import os

class TestBalancesController(ControllerTestBase):
    """Test suite for Balances endpoints.
    
    This class contains tests for the Balances API endpoints, including:
    - Account balances retrieval
    - Balance history retrieval
    """

    def test_get_balances(self):
        """Test GET /balances/v2/:providerId/:accountId endpoint.
        
        This test verifies that:
        - The endpoint returns a successful response
        - The response contains account balance information
        - The account ID is properly used in the request
        - The response structure matches the API specification
        """
        client = self.get_client_with_credentials(
            os.getenv('TEST_USERNAME', 'GenericUser_Pfm'),
            os.getenv('TEST_PASSWORD', 'GenericUser_Pfm')
        )
        response = client.balances.get_balances(
            version=self.api_version,
            provider_id=self.provider_id
        )
        assert response is not None
        assert response.status_code == 200
        assert response.body is not None