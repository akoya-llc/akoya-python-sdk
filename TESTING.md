# Akoya SDK Test Suite Guide

## Overview

This document describes the structure, architecture, and usage of the test suite for the Akoya SDK. It is intended for developers who want to understand, extend, or contribute to the test coverage of the SDK.

---

## Prerequisites

1. **Python 3.11 or higher**
2. **Git** for version control
3. **Playwright** for automated consent flow
4. **Environment Variables** (see Configuration section)

---

## Directory Layout

```
tests/
  endpoint_tests/
    controller_test_base.py
    test_account_info_controller.py
    test_balances_controller.py
    test_customers_controller.py
    test_investments_controller.py
    test_payments_controller.py
    test_statements_controller.py
    test_transactions_controller.py
    test_tax_controller.py
  auth_tests/
    test_error_scenarios.py
  http_response_catcher.py
```

- **endpoint_tests/**: Tests for each Akoya SDK controller, organized by product.
- **endpoint_tests/controller_test_base.py**: Base class for controller tests, handling client setup and authentication.
- **auth_tests/**: Contains tests for common authentication error scenarios, including specific error codes returned by the Akoya API.

---

## Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# OAuth 2.0 Client Credentials
OAUTH_CLIENT_ID=your_client_id
OAUTH_CLIENT_SECRET=your_client_secret
OAUTH_REDIRECT_URI=your_redirect_uri

# Akoya API Configuration
AKOYA_API_VERSION=v2 # e.g., v2
AKOYA_PROVIDER_ID=mikomo # e.g., mikomo (the bank connector ID)

# Akoya Environment (SANDBOX or PRODUCTION)
ENVIRONMENT=SANDBOX # or PRODUCTION

# Test User Credentials (for automated consent flow)
TEST_USERNAME=your_test_username
TEST_PASSWORD=your_test_password

# Akoya Connector and State (for consent flow)
CONNECTOR=your_connector
STATE=random_state_string

# Redirect URI for Playwright to wait for
RETURN_URL=your_redirect_uri
```

### GitHub Secrets

For CI/CD, add these variables as secrets in your GitHub repository:
- `OAUTH_CLIENT_ID`
- `OAUTH_CLIENT_SECRET`
- `AKOYA_API_VERSION`
- `AKOYA_PROVIDER_ID`
- `TEST_USERNAME`
- `TEST_PASSWORD`
- `CONNECTOR`
- `STATE`
- `RETURN_URL`
- `ENVIRONMENT`

---

## Test Architecture

- **Controller-based**: Each controller (e.g., Account Info, Balances, Transactions) has its own test file.
- **Test Methods**: Each method targets a specific endpoint, using request data and parameters as found in the official Postman collection.
- **Error Handling**: For endpoints with error scenarios (e.g., invalid token), tests simulate these by injecting invalid credentials.
- **Base Class**: All test classes inherit from `ControllerTestBase`, which manages client instantiation and authentication setup.
- **Consent Flow**: Automated using Playwright, runs only once per test session and reuses the token.

### Example Test (Unit)

```python
class TestBalancesController(ControllerTestBase):
    def test_get_balances(self, client):
        response = client.balances.get_balances(
            version="v2",
            provider_id="mikomo"
        )
        assert response is not None
        assert response.status_code == 200
        assert response.body is not None
```

---

## How to Add More Tests

1. **Identify the Controller**: Find the relevant controller test file in `tests/endpoint_tests/` (e.g., `test_payments_controller.py` for Payments endpoints).
2. **Add a Test Method**:
   - Use the naming convention: `test_<endpoint_description>`.
   - Use the request data (parameters, path, etc.) as in the Postman collection or API docs.
   - Use the `client` fixture provided by the base class.
3. **Example**:

```python
def test_get_new_feature(self, client):
    response = client.some_controller.get_new_feature(
        version="v2",
        provider_id="mikomo",
        # ...other params...
    )
    assert response is not None
    assert response.status_code == 200
    assert response.body is not None
```

4. **Error Scenarios**: To test error cases (e.g., invalid token), clone the client with an invalid token and assert that an exception is raised.

```python
def test_feature_with_invalid_token(self, client):
    invalid_client = client.__class__(config=client.config.clone_with(
        authorization_code_auth_credentials=client.config.authorization_code_auth_credentials.clone_with(
            oauth_token="invalid_token"
        )
    ))
    with pytest.raises(Exception):
        invalid_client.some_controller.get_new_feature(...)
```

5. **Run the Tests** to verify your additions (see below).

---

## How to Run the Test Suite

1. **Install Dependencies**  
   From the project root, install the requirements:
   ```bash
   pip install -r requirements.txt
   pip install -r test-requirements.txt
   ```

2. **Install Playwright**  
   ```bash
   python -m playwright install --with-deps
   ```

3. **Run All Tests**  
   From the project root, run:
   ```bash
   pytest
   ```
   This will discover and run all tests in the `tests/` directory.

4. **Run with Verbose Output**  
   ```bash
   pytest -v
   ```

5. **Run with Tracing**  
   ```bash
   pytest --tracing=retain-on-failure
   ```

6. **Run a Specific Test File**  
   ```bash
   pytest tests/endpoint_tests/test_balances_controller.py
   ```

7. **Run a Specific Test Method**  
   ```bash
   pytest tests/endpoint_tests/test_balances_controller.py::TestBalancesController::test_get_balances
   ```

---

## CI/CD Integration

The test suite is integrated with GitHub Actions for continuous integration. The workflow:

1. Sets up Python 3.11
2. Installs dependencies
3. Configures environment variables from secrets
4. Installs Playwright and its dependencies
5. Runs the test suite
6. Uploads test artifacts on failure

To view the workflow, see `.github/workflows/run-tests.yml`.

---

## Best Practices

- **Keep test data in sync** with the Postman collection and API documentation.
- **Use descriptive test names** for clarity.
- **Group related tests** in the appropriate controller test file.
- **Test both success and error scenarios** for robust coverage.
- **Reuse the base class** for consistent client setup and teardown.
- **Handle pagination** by extracting and using `prev` and `next` links from responses.
- **Use session-scoped fixtures** for the consent flow to avoid multiple authentications.

---

## Troubleshooting

1. **Authentication Issues**
   - Verify environment variables are set correctly
   - Check if the consent flow is completing successfully
   - Ensure the test user has the necessary permissions

2. **Playwright Issues**
   - Check if browsers are installed: `python -m playwright install --with-deps`
   - Run with tracing: `pytest --tracing=retain-on-failure`
   - Check the `test-results/` directory for traces

3. **Import Errors**
   - Ensure you're running from the project root
   - Use `PYTHONPATH=.` when running tests
   - Check if `__init__.py` files are present in all directories

4. **CI/CD Issues**
   - Verify all required secrets are set in GitHub
   - Check the workflow logs for detailed error messages
   - Review the uploaded artifacts for traces

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your tests
4. Run the test suite locally
5. Submit a pull request

---

**For more details on the SDK and API usage, see the main `README.md` and the `/doc` directory.** 