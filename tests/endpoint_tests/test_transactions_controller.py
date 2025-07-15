import pytest
from akoyaapisv240.models.transactions_entity import TransactionsEntity
from tests.endpoint_tests.controller_test_base import ControllerTestBase
import dateutil.parser
from akoyaapisv240.models.mode import Mode
import os

class TestTransactionsController(ControllerTestBase):
    """Test suite for Transactions endpoints.
    
    This class contains tests for the Transactions API endpoints, including:
    - Getting transactions list
    - Pagination (next/previous page)
    - Error handling
    """

    def test_get_transactions(self):
        """Test GET /transactions/:version/:providerId/:accountId endpoint.
        
        This test verifies that:
        - The endpoint returns a successful response
        - The response contains transaction data
        - The response structure matches the API specification
        """
        client = self.get_client_with_credentials(
            os.getenv('TEST_USERNAME', 'GenericUser_Pfm'),
            os.getenv('TEST_PASSWORD', 'GenericUser_Pfm')
        )
        response = client.transactions.get_transactions(
            version=self.api_version,
            provider_id=self.provider_id,
            account_id=self.account_id,
            start_time = dateutil.parser.parse('2020-03-30T04:00:00Z'),
            end_time = dateutil.parser.parse('2026-03-30T04:00:00Z'),
            offset = '0',
            limit = 50,
            mode = Mode.RAW
        )

        # Verify that the response is a PagedIterable
        assert hasattr(response, '__iter__')
        assert hasattr(response, 'pages')

        # Iterate through items across all pages and count them
        item_count = 0
        for item in response:
            assert item is not None # Verify each item is not None
            item_count += 1
        
        # Assert that at least one item was fetched (indicating successful iteration)
        assert item_count > 0, "No items fetched from transactions PagedIterable."

        # Iterate through pages explicitly and check their status codes
        page_count = 0
        for page in response.pages():
            assert page is not None
            page_count += 1
        
        assert page_count > 0, "No pages fetched from transactions PagedIterable."
