
# Investment Balance

*This model accepts additional fields of type Any.*

## Structure

`InvestmentBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `investment_account` | [`InvestmentBalances`](../../doc/models/investment-balances.md) | Optional | Data elements included with balances specific to investment accounts |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "investmentAccount": {
    "accountId": "accountId8",
    "accountType": "accountType8",
    "accountNumberDisplay": "accountNumberDisplay4",
    "currency": {
      "currencyCode": "currencyCode0",
      "currencyRate": 27.48,
      "originalCurrencyCode": "originalCurrencyCode4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    "description": "description8",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

