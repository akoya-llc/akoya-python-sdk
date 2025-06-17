
# Deposit Balance

## Structure

`DepositBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deposit_account` | [`DepositBalances`](../../doc/models/deposit-balances.md) | Optional | Data elements included with balances specific to deposit accounts |

## Example (as JSON)

```json
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
```

