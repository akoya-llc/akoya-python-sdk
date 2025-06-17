
# Loc Balance

## Structure

`LocBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loc_account` | [`LineOfCreditBalances`](../../doc/models/line-of-credit-balances.md) | Optional | Data elements included with balances specific to line of credit accounts |

## Example (as JSON)

```json
{
  "locAccount": {
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
```

