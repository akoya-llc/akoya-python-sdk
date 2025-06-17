
# Account Info Item

## Structure

`AccountInfoItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deposit_account` | [`DepositAccount`](../../doc/models/deposit-account.md) | Optional | Deposit Account |
| `loan_account` | [`LoanAccount`](../../doc/models/loan-account.md) | Optional | Loan Account |
| `loc_account` | [`AccountInformation`](../../doc/models/account-information.md) | Optional | Line of Credit Account |
| `investment_account` | [`InvestmentAccount`](../../doc/models/investment-account.md) | Optional | Investment Account |
| `insurance_account` | [`InsuranceAccount`](../../doc/models/insurance-account.md) | Optional | Insurance Account |
| `annuity_account` | [`AnnuityAccount`](../../doc/models/annuity-account.md) | Optional | Annuity Account |

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

