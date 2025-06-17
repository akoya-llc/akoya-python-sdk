# Statements

Statements

```python
statements_controller = client.statements
```

## Class Name

`StatementsController`

## Methods

* [Get-Statement-List](../../doc/controllers/statements.md#get-statement-list)
* [Get-Statements](../../doc/controllers/statements.md#get-statements)


# Get-Statement-List

Retrieve a list of available statements for the end-user's consented accounts. You may request a date range of up to two years of historical statements (maximum date ranges vary by provider).

The paginated response includes an array of statement information with the end-user's account id and statement details such as statement id, date, description, and status. The results also include links to GET the statement image.

```python
def get_statement_list(self,
                      account_id,
                      version,
                      provider_id,
                      start_time=None,
                      end_time=None,
                      offset='0',
                      limit=50,
                      x_akoya_interaction_type=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Template, Required | Account Identifier |
| `version` | `str` | Template, Required | Akoya major version number. Do not use minor version numbers. For instance, use v2 and not v2.2 |
| `provider_id` | `str` | Template, Required | Id of provider |
| `start_time` | `date` | Query, Optional | Start date for use in retrieval of statements (ISO 8601) |
| `end_time` | `date` | Query, Optional | End date for use in retrieval of statements (ISO 8601) |
| `offset` | `str` | Query, Optional | The number of items to skip before the first in the response. The default is 0.<br><br>**Default**: `'0'` |
| `limit` | `int` | Query, Optional | The maximum number of items to be returned in the response. The default is 50.<br><br>**Default**: `50` |
| `x_akoya_interaction_type` | [`InteractionTypeEnum`](../../doc/models/interaction-type-enum.md) | Header, Optional | Optional but recommended header to include with each data request.<br>Allowed values are `user` or `batch`.<br>`user` indicates a request is prompted by an end-user action.<br>`batch` indicates the request is part of a batch process. |

## Response Type

[`PaginatedArray`](../../doc/models/paginated-array.md)

## Example Usage

```python
account_id = ':accountId'

version = 'v2'

provider_id = 'mikomo'

start_time = dateutil.parser.parse('2020-03-30').date()

end_time = dateutil.parser.parse('2021-03-30').date()

offset = '0'

limit = 50

result = statements_controller.get_statement_list(
    account_id,
    version,
    provider_id,
    start_time=start_time,
    end_time=end_time,
    offset=offset,
    limit=limit
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Start or end date value is not in the ISO 8601 format. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 404 | 404 - Not found | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 405 | Method Not Allowed | `APIException` |
| 408 | Request timed out (round trip call took >10 seconds). | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 500 | Catch-all exception where request was not processed due to an internal outage/issue. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 501 | FdxVersion in header is not implemented. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 503 | System is down for maintenance. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Get-Statements

Retrieve a specific account statement file. Use [HTTP Accept request-header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html) to specify desired content types.

For the initial launch, only PDF statements are supported. PDFs are returned in the response.

### cURL request

We recommend using the auto-generated cURL request with the {idToken}, accountId, providerId, statementId, and version with an added cURL parameter to return the output to a file. For example:

```curl
curl --request GET --url https://sandbox-products.ddp.akoya.com/statements/v2/mikomo/513815781465/P9CvLPKDaFRMbNDkhu1 --header "accept: application/pdf" --header "authorization: Bearer {idtoken}" --output example.pdf
```

```python
def get_statements(self,
                  account_id,
                  version,
                  provider_id,
                  statement_id,
                  x_akoya_interaction_type=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Template, Required | Account Identifier |
| `version` | `str` | Template, Required | Akoya major version number. Do not use minor version numbers. For instance, use v2 and not v2.2 |
| `provider_id` | `str` | Template, Required | Id of provider |
| `statement_id` | `str` | Template, Required | Statement Identifier |
| `x_akoya_interaction_type` | [`InteractionTypeEnum`](../../doc/models/interaction-type-enum.md) | Header, Optional | Optional but recommended header to include with each data request.<br>Allowed values are `user` or `batch`.<br>`user` indicates a request is prompted by an end-user action.<br>`batch` indicates the request is part of a batch process. |

## Response Type

`Any`

## Example Usage

```python
account_id = ':accountId'

version = 'v2'

provider_id = 'mikomo'

statement_id = 'statementId'

result = statements_controller.get_statements(
    account_id,
    version,
    provider_id,
    statement_id
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Statement is processing and is not yet available. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 404 | Account exists but contains no statements. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 405 | Method Not Allowed | `APIException` |
| 406 | Content Type not Supported | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 408 | Request timed out (round trip call took >10 seconds). | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 500 | Catch-all exception where request was not processed due to an internal outage/issue. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 501 | FdxVersion in header is not implemented. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 503 | System is down for maintenance. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |

