
# Akoya Account Info Product

An optionally paginated array of accounts

## Structure

`AkoyaAccountInfoProduct`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accounts` | List[[DepositAccountInfo](../../doc/models/deposit-account-info.md) \| [LoanAccountInfo](../../doc/models/loan-account-info.md) \| [LocAccountInfo](../../doc/models/loc-account-info.md) \| [InvestmentAccountInfo](../../doc/models/investment-account-info.md) \| [InsuranceAccountInfo](../../doc/models/insurance-account-info.md) \| [AnnuityAccountInfo](../../doc/models/annuity-account-info.md)] \| None | Optional | This is List of a container for any-of cases. |

## Example (as JSON)

```json
{
  "accounts": [
    {
      "depositAccount": {
        "accountId": "accountId0",
        "accountType": "accountType0",
        "accountNumberDisplay": "accountNumberDisplay6",
        "currency": {
          "currencyCode": "currencyCode0",
          "currencyRate": 27.48,
          "originalCurrencyCode": "originalCurrencyCode4"
        },
        "description": "description0"
      }
    },
    {
      "depositAccount": {
        "accountId": "accountId0",
        "accountType": "accountType0",
        "accountNumberDisplay": "accountNumberDisplay6",
        "currency": {
          "currencyCode": "currencyCode0",
          "currencyRate": 27.48,
          "originalCurrencyCode": "originalCurrencyCode4"
        },
        "description": "description0"
      }
    }
  ]
}
```

