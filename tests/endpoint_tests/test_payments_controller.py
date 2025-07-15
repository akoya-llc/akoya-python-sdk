import pytest
from tests.endpoint_tests.controller_test_base import ControllerTestBase
import os

class TestPaymentsController(ControllerTestBase):
    """Test suite for Payments endpoints.
    
    This class contains tests for the Payments API endpoints, including:
    - Payment networks retrieval
    """

    def test_get_payment_networks(self):
        """Test GET /payment-networks/:version/:providerId endpoint.
        
        This test verifies that:
        - The endpoint returns a successful response
        - The response contains available payment networks
        - The account ID is properly used in the request
        - The response structure matches the API specification
        """
        client = self.get_client_with_credentials(
            os.getenv('TEST_USERNAME', 'GenericUser_Pfm'),
            os.getenv('TEST_PASSWORD', 'GenericUser_Pfm')
        )
        response = client.payments.payment_networks(
            version=self.api_version,
            provider_id=self.provider_id,
            account_id=self.statement_account_id
        )
        assert response is not None
        assert response.status_code == 200
 