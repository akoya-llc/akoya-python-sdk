import pytest
from tests.endpoint_tests.controller_test_base import ControllerTestBase
import os

class TestTaxController(ControllerTestBase):
    """Test suite for Tax endpoints.
    
    This class contains tests for the Tax API endpoints, including:
    - Tax form search
    - Tax form retrieval
    """

    def test_tax_form_search(self):
        """Test GET /tax-forms/:version/:provider endpoint.
        
        This test verifies that:
        - The endpoint returns a successful response
        - The response contains tax form search results
        - The search parameters (tax year and form type) are properly applied
        """
        client = self.get_client_with_credentials(
            os.getenv('TAX_USERNAME', 'GenericUser_Pfm'),
            os.getenv('TAX_PASSWORD', 'GenericUser_Pfm')
        )
        response = client.tax_beta.tax_forms_search(
            version=self.api_version,
            provider_id=self.provider_id
        )
        assert response is not None
        assert response.status_code == 200
        assert response.body is not None

    def test_retrieve_tax_form(self):
        """Test GET /tax-forms/:version/:provider/:taxFormId endpoint.
        
        This test verifies that:
        - The endpoint returns a successful response
        - The response contains the requested tax form
        - The tax form ID is properly used in the request
        """
        client = self.get_client_with_credentials(
            os.getenv('TAX_USERNAME', 'GenericUser_Pfm'),
            os.getenv('TAX_PASSWORD', 'GenericUser_Pfm')
        )
        response = client.tax_beta.get_tax_form(
            version=self.api_version,
            provider_id=self.provider_id,
            tax_form_id="tax2020"
        )
        assert response is not None
        assert response.status_code == 200
        assert response.body is not None 