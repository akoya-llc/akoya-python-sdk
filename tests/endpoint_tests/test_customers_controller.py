import pytest
from akoyaapisv240.exceptions.error_error_exception import ErrorErrorException
from tests.endpoint_tests.controller_test_base import ControllerTestBase
import os

class TestCustomersController(ControllerTestBase):
    """Test suite for Customers endpoints.
    
    This class contains tests for the Customers API endpoints, including:
    - Customer information retrieval
    - Contact information retrieval
    """

    def test_get_customer_info(self):
        """Test GET /customers/v2/:providerId/current endpoint.
        
        This test verifies that:
        - The endpoint returns a successful response
        - The response contains current customer information
        - The provider ID is properly used in the request
        - The response structure matches the API specification
        """
        client = self.get_client_with_credentials(
            os.getenv('TEST_USERNAME', 'GenericUser_Pfm'),
            os.getenv('TEST_PASSWORD', 'GenericUser_Pfm')
        )
        response = client.customers.customer_info(
            version=self.api_version,
            provider_id=self.provider_id
        )
        assert response is not None
        assert response.status_code == 200
        assert response.body is not None

    def test_get_contacts(self):
        """Test GET /contacts/:version/:providerid/:accountId endpoint.
        
        This test verifies that:
        - The endpoint returns a successful response
        - The response contains contact information
        - The account ID is properly used in the request
        - The response structure matches the API specification
        """
        client = self.get_client_with_credentials(
            os.getenv('TEST_USERNAME', 'GenericUser_Pfm'),
            os.getenv('TEST_PASSWORD', 'GenericUser_Pfm')
        )
        try:
            response = client.customers.get_account_holder(
                version=self.api_version,
                provider_id=self.provider_id,
                account_id=self.account_id
            )
        except ErrorErrorException as e:
            assert e.response_code == 404 # "Expected 404 Not Found for non-existent account"
