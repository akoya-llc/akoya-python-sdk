
# Investments Details

## Structure

`InvestmentsDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accounts` | List[[InvestmentBalanceInfo](../../doc/models/investment-balance-info.md) \| [DepositBalanceInfo](../../doc/models/deposit-balance-info.md) \| [LoanBalanceInfo](../../doc/models/loan-balance-info.md) \| [LocBalanceInfo](../../doc/models/loc-balance-info.md) \| [InsuranceBalanceInfo](../../doc/models/insurance-balance-info.md) \| [AnnuityBalanceInfo](../../doc/models/annuity-balance-info.md)] \| None | Optional | This is List of a container for any-of cases. |

## Example (as JSON)

```json
{
  "accounts": [
    {
      "investmentAccount": {
        "accountId": "accountId8",
        "accountType": "accountType8",
        "accountNumberDisplay": "accountNumberDisplay4",
        "currency": {
          "currencyCode": "currencyCode0",
          "currencyRate": 27.48,
          "originalCurrencyCode": "originalCurrencyCode4"
        },
        "description": "description8"
      }
    },
    {
      "investmentAccount": {
        "accountId": "accountId8",
        "accountType": "accountType8",
        "accountNumberDisplay": "accountNumberDisplay4",
        "currency": {
          "currencyCode": "currencyCode0",
          "currencyRate": 27.48,
          "originalCurrencyCode": "originalCurrencyCode4"
        },
        "description": "description8"
      }
    },
    {
      "investmentAccount": {
        "accountId": "accountId8",
        "accountType": "accountType8",
        "accountNumberDisplay": "accountNumberDisplay4",
        "currency": {
          "currencyCode": "currencyCode0",
          "currencyRate": 27.48,
          "originalCurrencyCode": "originalCurrencyCode4"
        },
        "description": "description8"
      }
    }
  ]
}
```

