
# Getting Started with Akoya APIs v2.4.0

## Introduction

Akoya product APIs for data access. Default servers are set for the Akoya sandbox environment.

Akoya APIs include the following updates:

- v2.4.0
  - Added Tax product
- v2.3.0
  - Removed erroneous `accountId` query param from Taxlots endpoint
  - Added TaxLots endpoint
- v2.2.2
  - Added mode query parameter to Account Information, Balances, Investments, and Transactions to support standard mode.
  - Edited callouts for Account Holder endpoint
- v2.2.1
  - Fixed typo in `accountIds` query parameter for `/accounts-info`, `/balances`, `/accounts`
  - Added security method for `Account holder information` to bear token. Missing method defaulted to basic auth.
  - Added examples and descriptions to some schemas
  - Added HTTP status `429` FDX error `1207`.
- v2.2 Additions
  - Added optional `x-akoya-interaction-type` header to all endpoints to specify if a request is part of a batch process
  - Update of tags to organize endpoints by Akoya product
  - `206` response added to `/accounts-info`, `/balances`, `/accounts`
- v2.1 New Statements product and Customers product updated with additional endpoint, `Account holder information`.
- v2.0 Launch of Akoya products: Account Info, Balances, Investments, Transactions, Payments, Customers.

## Building

You must have Python `3.7+` installed on your system to install and run this SDK. This SDK package depends on other Python packages like pytest, etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK. To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Akoya-Python&step=installDependencies)

## Installation

The following section explains how to use the akoya library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Akoya-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Akoya-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Akoya-Python&projectName=akoya&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Akoya-Python&projectName=akoya&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Akoya-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Akoya-Python&projectName=akoya&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Akoya-Python&projectName=akoya&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from akoya.akoya_client import AkoyaClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Akoya-Python&projectName=akoya&libraryName=akoya.akoya_client&className=AkoyaClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Akoya-Python&projectName=akoya&libraryName=akoya.akoya_client&className=AkoyaClient&step=runProject)

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| environment | `Environment` | The API environment. <br> **Default: `Environment.SANDBOX`** |
| http_client_instance | `HttpClient` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 60** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| logging_configuration | [`LoggingConfiguration`](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/logging-configuration.md) | The SDK logging configuration for API calls |
| authorization_code_auth_credentials | [`AuthorizationCodeAuthCredentials`](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/auth/oauth-2-authorization-code-grant.md) | The credential object for OAuth 2 Authorization Code Grant |

The API client can be initialized as follows:

```python
client = AkoyaClient(
    authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
        oauth_client_id='OAuthClientId',
        oauth_client_secret='OAuthClientSecret',
        oauth_redirect_uri='OAuthRedirectUri',
        oauth_scopes=[
            OauthScope.OPENID,
            OauthScope.PROFILE
        ]
    ),
    environment=Environment.SANDBOX,
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)
```

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| Sandbox | **Default** |
| Production | - |

## Authorization

This API uses the following authentication schemes.

* [`acgAuth (OAuth 2 Authorization Code Grant)`](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/auth/oauth-2-authorization-code-grant.md)

## List of APIs

* [Accountinformation](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/controllers/accountinformation.md)
* [Tax Beta](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/controllers/tax-beta.md)
* [Balances](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/controllers/balances.md)
* [Customers](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/controllers/customers.md)
* [Investments](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/controllers/investments.md)
* [Payments](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/controllers/payments.md)
* [Statements](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/controllers/statements.md)
* [Transactions](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/controllers/transactions.md)

## SDK Infrastructure

### Configuration

* [AbstractLogger](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/abstract-logger.md)
* [LoggingConfiguration](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/logging-configuration.md)
* [RequestLoggingConfiguration](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/request-logging-configuration.md)
* [ResponseLoggingConfiguration](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/response-logging-configuration.md)

### HTTP

* [HttpResponse](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/http-response.md)
* [HttpRequest](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/http-request.md)

### Utilities

* [ApiResponse](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/api-response.md)
* [PagedIterable](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/paged-iterable.md)
* [LinkPagedResponse](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/link-paged-response.md)
* [CursorPagedResponse](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/cursor-paged-response.md)
* [OffsetPagedResponse](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/offset-paged-response.md)
* [NumberPagedResponse](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/number-paged-response.md)
* [ApiHelper](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/api-helper.md)
* [HttpDateTime](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/http-date-time.md)
* [RFC3339DateTime](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/rfc3339-date-time.md)
* [UnixDateTime](https://www.github.com/akoya-llc/akoya-python-sdk/tree/0.2.0/doc/unix-date-time.md)

