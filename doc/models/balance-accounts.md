
# Balance Accounts

## Structure

`BalanceAccounts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deposit_account` | [`DepositBalances`](../../doc/models/deposit-balances.md) | Optional | Data elements included with balances specific to deposit accounts |
| `loan_account` | [`LoanBalances`](../../doc/models/loan-balances.md) | Optional | Data elements included with balances specific to loan accounts |
| `loc_account` | [`LineOfCreditBalances`](../../doc/models/line-of-credit-balances.md) | Optional | Data elements included with balances specific to line of credit accounts |
| `investment_account` | [`InvestmentBalances`](../../doc/models/investment-balances.md) | Optional | Data elements included with balances specific to investment accounts |
| `insurance_account` | [`InsuranceBalances`](../../doc/models/insurance-balances.md) | Optional | Data elements included with balances specific to insurance accounts |
| `annuity_account` | [`AnnuityBalances`](../../doc/models/annuity-balances.md) | Optional | Data elements included with balances specific to annuity accounts |

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
  },
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
  },
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
  },
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
  },
  "insuranceAccount": {
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
```

