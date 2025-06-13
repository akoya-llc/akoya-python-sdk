# Investments

Investments

```python
investments_controller = client.investments
```

## Class Name

`InvestmentsController`

## Methods

* [Get-Accounts](../../doc/controllers/investments.md#get-accounts)
* [Get-Taxlots](../../doc/controllers/investments.md#get-taxlots)


# Get-Accounts

Get detailed account information that includes Akoya products Account Info and Balances for all account types (annunity, deposit, insurance, investments, line of credit, and loan) and adds the Investments product to investment accounts including contributions, holdings, vesting information, and more.

To view the response schema, select the `200` response below. Then pick an option for annuity, deposit, insurance, investment, loan, and line of credit account types.

For an example payload response, see the `200` example response below the `Try it` feature. The example is from an investment account but all account types are supported and returned by this endpoint.

> 🛑
> 
> The *id_token* should be used as the bearer token with this call.

Use the `mode` query param to receive FDX-aligned, standardized data values (Beta). For example:

`https://sandbox-products.ddp.akoya.com/accounts/v2/mikomo?mode=standard`

`mode` is available in both sandbox and production.

`mode` is supported by a subset of providers. Log into the [Data Recipient Hub](https://recipient.ddp.akoya.com/login) and click [here](https://recipient.ddp.akoya.com/support/article/kA0Uw00000015GzKAI) to view a list of all providers supporting the `mode` parameter.

```python
def get_accounts(self,
                version,
                provider_id,
                x_akoya_interaction_type=None,
                mode=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | Akoya major version number. Do not use minor version numbers. For instance, use v2 and not v2.2 |
| `provider_id` | `str` | Template, Required | Id of provider |
| `x_akoya_interaction_type` | [`InteractionType`](../../doc/models/interaction-type.md) | Header, Optional | Optional but recommended header to include with each data request.<br>Allowed values are `user` or `batch`.<br>`user` indicates a request is prompted by an end-user action.<br>`batch` indicates the request is part of a batch process. |
| `mode` | [`Mode`](../../doc/models/mode.md) | Query, Optional | BETA. Default is raw. Use standard for FDX-aligned, standardized data values. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InvestmentsDetails`](../../doc/models/investments-details.md).

## Example Usage

```python
version = 'v2'

provider_id = 'mikomo'

mode = Mode.RAW

result = investments_controller.get_accounts(
    version,
    provider_id,
    mode=mode
)
```

## Example Response *(as JSON)*

```json
{
  "accounts": [
    {
      "investmentAccount": {
        "accountId": "839502593",
        "accountType": "College Savings",
        "availableCashBalance": 0,
        "balanceAsOf": "2022-03-16T04:00:00Z",
        "balanceType": "ASSET",
        "currency": {
          "currencyCode": "USD"
        },
        "currentValue": 52672.49,
        "holdings": [
          {
            "assetClasses": [
              {
                "assetClass": "DOMESTICBOND",
                "percent": 0
              }
            ],
            "cashAccount": false,
            "marketValue": 52672.49,
            "mutualFundSecurity": {
              "mutualFundType": "OPENEND",
              "reinvestCapitalGains": true,
              "reinvestDividends": true,
              "unitsStreet": 0,
              "unitsUser": 0,
              "yield": 0,
              "yieldAsOfDate": "2019-08-24T14:15:22Z"
            },
            "positionType": "LONG",
            "purchasedPrice": 18.42,
            "securityIdType": "ISIN",
            "units": 2088.521
          }
        ],
        "marginBalance": 0,
        "nickname": "529 for Kid"
      }
    },
    {
      "investmentAccount": {
        "accountId": "5426873",
        "accountNumberDisplay": "...7054",
        "accountType": "BROKERAGE",
        "allowedCheckWriting": false,
        "availableCashBalance": 0,
        "balanceList": [
          {
            "balanceDate": "2021-07-06",
            "balanceDescription": "Margin Call",
            "balanceName": "MARGINCALL",
            "balanceType": "AMOUNT",
            "balanceValue": 0,
            "currency": {
              "currencyCode": "USD"
            }
          },
          {
            "balanceDate": "2021-07-06",
            "balanceDescription": "Fed Call",
            "balanceName": "FEDCALL",
            "balanceType": "AMOUNT",
            "balanceValue": 0,
            "currency": {
              "currencyCode": "USD"
            }
          },
          {
            "balanceDate": "2021-07-06",
            "balanceDescription": "Intra Day",
            "balanceName": "INTRADAY",
            "balanceType": "AMOUNT",
            "balanceValue": 0,
            "currency": {
              "currencyCode": "USD"
            }
          },
          {
            "balanceDate": "2021-07-05",
            "balanceDescription": "Prior Day",
            "balanceName": "PRIORDAY",
            "balanceType": "AMOUNT",
            "balanceValue": 0,
            "currency": {
              "currencyCode": "USD"
            }
          }
        ],
        "currency": {
          "currencyCode": "USD"
        },
        "lastActivityDate": "2021-07-06T00:00:00Z",
        "margin": false,
        "marginBalance": 0,
        "nickname": "Self-Directed",
        "shortBalance": 0,
        "status": "OPEN",
        "transactionsIncluded": false
      }
    },
    {
      "depositAccount": {
        "accountId": "g833202fb0866d0ad83472c429",
        "accountNumberDisplay": "xxxxxxxx0071",
        "accountType": "CHECKING",
        "availableBalance": 106717.06,
        "balanceAsOf": "2022-04-24T14:15:22Z",
        "balanceType": "ASSET",
        "currency": {
          "currencyCode": "USD"
        },
        "currentBalance": 106717.06,
        "description": "Checking Plus",
        "fiAttributes": [
          {
            "name": "accountOpenedDate",
            "value": "2020-04-23"
          },
          {
            "name": "interestPaidLastYear",
            "value": "3.20"
          }
        ],
        "interestRate": 0.0125,
        "interestRateAsOf": "2022-04-24T14:15:22Z",
        "interestRateType": "FIXED",
        "interestYtd": 20.33,
        "lastActivityDate": "2022-04-24T14:15:22Z",
        "lineOfBusiness": "Personal",
        "nickname": "Nickname Checking Plus 0071",
        "productName": "Checking Plus",
        "status": "OPEN",
        "transferIn": true,
        "transferOut": true
      }
    },
    {
      "depositAccount": {
        "accountId": "5dbda8de96eeff05f23934523a1fc258",
        "accountNumberDisplay": "xxxx0134",
        "accountType": "CHECKING",
        "annualPercentageYield": 0,
        "availableBalance": 0,
        "balanceAsOf": "2022-04-24T14:15:22Z",
        "currency": {
          "currencyCode": "USD"
        },
        "currentBalance": 0,
        "description": "Virtual Wallet Student Reserve",
        "interestRateAsOf": "2022-04-24T14:15:22Z",
        "interestRateType": "FIXED",
        "lastActivityDate": "2022-04-01T10:05:00Z",
        "lineOfBusiness": "LBRB",
        "openingDayBalance": 0,
        "productName": "Virtual Wallet Student Reserve",
        "transactionsIncluded": false
      }
    },
    {
      "depositAccount": {
        "accountId": "11719ae5-2399-1278-e43c-43f24abb3058",
        "accountType": "CD",
        "annualPercentageYield": 0.75,
        "availableBalance": 6808.29,
        "balanceAsOf": "2021-04-07T10:20:43.276Z",
        "balanceType": "ASSET",
        "currency": {
          "currencyCode": "USD",
          "originalCurrencyCode": "USD"
        },
        "currentBalance": 6808.29,
        "description": "Certificate of Deposit",
        "fiAttributes": [
          {
            "name": "eStatements",
            "value": "False"
          },
          {
            "name": "interestPaidLastYear",
            "value": "50.72"
          },
          {
            "name": "isTransactionsSupported",
            "value": "False"
          },
          {
            "name": "issueDate",
            "value": "2019-03-21T00:00:00.000Z"
          },
          {
            "name": "interestPayoutFrequency",
            "value": "Semi-Annually (And At Maturity)"
          }
        ],
        "interestRate": 0.75,
        "interestYtd": 25.24,
        "lineOfBusiness": "CONSUMER",
        "maturityDate": "2024-03-21T00:00:00Z",
        "nickname": "Certificate of Deposit - 3691",
        "openingDayBalance": 2000,
        "parentAccountId": "11719ae5-2399-1278-e43c-43f24abb3058",
        "status": "OPEN",
        "term": 60,
        "transactionsIncluded": false,
        "transferIn": false,
        "transferOut": false
      }
    },
    {
      "depositAccount": {
        "accountId": "33fbd9e5-9cc3-3d7d-15b3-70d97d87ca1d",
        "accountType": "SAVINGS",
        "availableBalance": 20608.9,
        "balanceAsOf": "2021-04-07T10:08:11.833Z",
        "balanceType": "ASSET",
        "currency": {
          "currencyCode": "USD",
          "originalCurrencyCode": "USD"
        },
        "currentBalance": 20608.9,
        "description": "Savings",
        "fiAttributes": [
          {
            "name": "eStatements",
            "value": "True"
          }
        ],
        "interestRate": 0.01,
        "interestYtd": 0.29,
        "lineOfBusiness": "CONSUMER",
        "nickname": "Savings - 8537",
        "openingDayBalance": 20608.9,
        "parentAccountId": "33fbd9e5-9cc3-3d7d-15b3-70d97d87ca1d",
        "status": "OPEN",
        "transactionsIncluded": false
      }
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Input | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 401 | Customer not authorized. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 404 | 701 - Tax Lots not found. The `holdingId` may be wrong. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 405 | Method Not Allowed | `ApiException` |
| 406 | Content Type not Supported | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 408 | Request timed out (round trip call took >10 seconds). | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 429 | 1207 - Too many requests | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 500 | Internal Server Error. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 501 | FdxVersion in header is not implemented. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 503 | System is down for maintenance. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Get-Taxlots

The taxlots API allows you to retrieve tax lots of consumer-permissioned accounts.

> 🛑
> 
> The *id_token* should be used as the bearer token with this call.

```python
def get_taxlots(self,
               version,
               provider_id,
               account_id,
               holding_id,
               x_akoya_interaction_type=None,
               offset=None,
               limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | Akoya major version number. Do not use minor version numbers. For instance, use v2 and not v2.2 |
| `provider_id` | `str` | Template, Required | Id of provider |
| `account_id` | `str` | Template, Required | Account Identifier |
| `holding_id` | `str` | Template, Required | Consumer's holdingId under investments |
| `x_akoya_interaction_type` | [`InteractionType`](../../doc/models/interaction-type.md) | Header, Optional | Optional but recommended header to include with each data request.<br>Allowed values are `user` or `batch`.<br>`user` indicates a request is prompted by an end-user action.<br>`batch` indicates the request is part of a batch process. |
| `offset` | `str` | Query, Optional | The number of items to skip before the first in the response. The default is 0 |
| `limit` | `str` | Query, Optional | The maximum number of items to be returned in the response. The default is 50 |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TaxlotsResponse`](../../doc/models/taxlots-response.md).

## Example Usage

```python
version = 'v2'

provider_id = 'mikomo'

account_id = 'accountId0'

holding_id = 'holdingId2'

result = investments_controller.get_taxlots(
    version,
    provider_id,
    account_id,
    holding_id
)
```

## Example Response *(as JSON)*

```json
{
  "accountId": "string",
  "holding": {
    "holdingId": "string",
    "securityId": "string",
    "securityIdType": "ISIN",
    "taxLots": [
      {
        "originalPurchaseDate": "2024-10-14T18:16:22Z",
        "quantity": 0,
        "purchasedPrice": 0,
        "costBasis": 0,
        "currentValue": 0,
        "positionType": "LONG"
      }
    ]
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Customer not authorized. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 403 | Incorrect providerId or no subscription to provider. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 404 | 701 - Tax Lots not found. The `holdingId` may be wrong. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 405 | Method Not Allowed | `ApiException` |
| 408 | Request timed out (round trip call took >10 seconds). | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |

