
# Loan Balance Info

## Structure

`LoanBalanceInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `loan_account` | [`LoanBalances`](../../doc/models/loan-balances.md) | Optional | Data elements included with balances specific to loan accounts |

## Example (as JSON)

```json
{
  "loanAccount": {
    "accountId": "accountId6",
    "accountType": "accountType6",
    "accountNumberDisplay": "accountNumberDisplay2",
    "currency": {
      "currencyCode": "currencyCode0",
      "currencyRate": 27.48,
      "originalCurrencyCode": "originalCurrencyCode4"
    },
    "description": "description6"
  }
}
```

