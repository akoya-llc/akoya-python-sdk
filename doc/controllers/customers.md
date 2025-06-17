# Customers

Customers

```python
customers_controller = client.customers
```

## Class Name

`CustomersController`

## Methods

* [Customer-Info](../../doc/controllers/customers.md#customer-info)
* [Get-Account-Holder](../../doc/controllers/customers.md#get-account-holder)


# Customer-Info

This product supports use cases such as payment enablement, account opening, and identity verification. Responses return information about the authorized end-user, the customer associated with the `id_token` used in the call. This information may include, but is not limited to, the customer identifier, name, email, address, and phone number.

<br>
To see the response schema, select the `200` response below. For an example payload response, see the `200` example response below the *Try it* feature.

This product requires consumer consent to share all account holder information.

> 🛑 The `id_token` should be used as the bearer token with this call.

```python
def customer_info(self,
                 version,
                 provider_id,
                 x_akoya_interaction_type=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | Akoya major version number. Do not use minor version numbers. For instance, use v2 and not v2.2 |
| `provider_id` | `str` | Template, Required | Id of provider |
| `x_akoya_interaction_type` | [`InteractionTypeEnum`](../../doc/models/interaction-type-enum.md) | Header, Optional | Optional but recommended header to include with each data request.<br>Allowed values are `user` or `batch`.<br>`user` indicates a request is prompted by an end-user action.<br>`batch` indicates the request is part of a batch process. |

## Response Type

[`Customer`](../../doc/models/customer.md)

## Example Usage

```python
version = 'v2'

provider_id = 'mikomo'

result = customers_controller.customer_info(
    version,
    provider_id
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 405 | Method Not Allowed | `APIException` |
| 408 | Request timed out (round trip call took >10 seconds). | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |


# Get-Account-Holder

This product supports use cases such as payment enablement, account opening, identity verification,or lending & credit enhancement. Responses return information about the authorized consumer, the customer associated with the `id_token` used in the call, and the relationship specific to the provided `accountId`.

> 📌 Please note!
> 
> This endpoint provides additional information which may not be required for your use case, making it inefficient compared to the [/customer info](https://docs.akoya.com/reference/customer-info) endpoint. Please refer to to the [Customers guide](https://docs.akoya.com/reference/customers) for more information about this endpoint.

Get account holder information. Based on FDX 5.2.1.

This product requires consumer consent to share all account holder information.

> 🛑 The `id_token` should be used as the bearer token with this call.

```python
def get_account_holder(self,
                      account_id,
                      version,
                      provider_id,
                      x_akoya_interaction_type=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Template, Required | Account Identifier |
| `version` | `str` | Template, Required | Akoya major version number. Do not use minor version numbers. For instance, use v2 and not v2.2 |
| `provider_id` | `str` | Template, Required | Id of provider |
| `x_akoya_interaction_type` | [`InteractionTypeEnum`](../../doc/models/interaction-type-enum.md) | Header, Optional | Optional but recommended header to include with each data request.<br>Allowed values are `user` or `batch`.<br>`user` indicates a request is prompted by an end-user action.<br>`batch` indicates the request is part of a batch process. |

## Response Type

[`AccountContactEntity`](../../doc/models/account-contact-entity.md)

## Example Usage

```python
account_id = ':accountId'

version = 'v2'

provider_id = 'mikomo'

result = customers_controller.get_account_holder(
    account_id,
    version,
    provider_id
)
```

## Example Response *(as JSON)*

```json
{
  "holders": [
    {
      "customerId": "string",
      "name": {
        "first": "string",
        "middle": "string",
        "last": "string",
        "prefix": "string",
        "suffix": "string",
        "company": "string"
      },
      "businessCustomer": {
        "name": "string",
        "registeredAgents": [
          {
            "first": "string",
            "middle": "string",
            "last": "string",
            "prefix": "string",
            "suffix": "string",
            "company": "string"
          }
        ],
        "registeredId": "string",
        "industryCode": {
          "type": "string",
          "code": "string"
        },
        "domicile": {
          "region": "string",
          "country": "string"
        }
      },
      "addresses": [
        {
          "line1": "string",
          "line2": "string",
          "line3": "string",
          "city": "string",
          "state": "string",
          "region": "string",
          "postalCode": "string",
          "country": "string",
          "type": "string"
        }
      ],
      "telephones": [
        {
          "number": "string",
          "type": "HOME",
          "country": "string"
        }
      ],
      "email": [
        "string"
      ],
      "accounts": [
        {
          "accountId": "string",
          "relationship": "AUTHORIZED_USER"
        }
      ],
      "relationship": "AUTHORIZED_USER"
    }
  ],
  "emails": [
    "string"
  ],
  "addresses": [
    {
      "line1": "string",
      "line2": "string",
      "line3": "string",
      "city": "string",
      "state": "string",
      "region": "string",
      "postalCode": "string",
      "country": "US",
      "type": "string"
    }
  ],
  "telephones": [
    {
      "type": "HOME",
      "country": "US",
      "number": "8675309"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 405 | Method Not Allowed | `APIException` |
| 408 | Request timed out (round trip call took >10 seconds). | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |

