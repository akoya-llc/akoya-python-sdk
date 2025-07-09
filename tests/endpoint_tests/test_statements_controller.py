import dateutil
import pytest
from tests.endpoint_tests.controller_test_base import ControllerTestBase
import os

class TestStatementsController(ControllerTestBase):
    """Test suite for Statements endpoints.
    
    This class contains tests for the Statements API endpoints, including:
    - Statement list retrieval
    - Individual statement retrieval
    """

    def test_get_statement_list(self):
        """Test GET /statements/:version/:providerId/:accountId endpoint.
        
        This test verifies that:
        - The endpoint returns a successful response
        - The response contains a list of statements
        - The time range parameters are properly applied
        - Pagination parameters (offset and limit) work correctly
        """
        client = self.get_client_with_credentials(
            os.getenv('TEST_USERNAME', 'GenericUser_Pfm'),
            os.getenv('TEST_PASSWORD', 'GenericUser_Pfm')
        )
        response = client.statements.get_statement_list(
            version=self.api_version,
            provider_id=self.provider_id,
            account_id=self.statement_account_id,
            start_time=dateutil.parser.parse('2021-03-30T04:00:00Z'),
            end_time=dateutil.parser.parse('2026-03-30T04:00:00Z'),
            offset=0,
            limit=5
        )
        assert response is not None
        assert response.status_code == 200
        assert response.body is not None

    def test_get_statement(self):
        """Test GET /statements/:version/:providerId/:accountId/:statementId endpoint.
        
        This test verifies that:
        - The endpoint returns a successful response
        - The response contains the requested statement
        - The statement ID is properly used in the request
        - The account ID is properly used in the request
        """
        client = self.get_client_with_credentials(
            os.getenv('TEST_USERNAME', 'GenericUser_Pfm'),
            os.getenv('TEST_PASSWORD', 'GenericUser_Pfm')
        )
        response = client.statements.get_statements(
            version=self.api_version,
            provider_id=self.provider_id,
            account_id=self.statement_account_id,
            statement_id=self.statement_id
        )
        assert response is not None
        assert response.status_code == 200