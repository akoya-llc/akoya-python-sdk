
# Transaction Item

## Structure

`TransactionItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deposit_transaction` | [`DepositTransaction`](../../doc/models/deposit-transaction.md) | Optional | Deposit transaction |
| `loan_transaction` | [`LoanTransaction`](../../doc/models/loan-transaction.md) | Optional | Loan Transaction |
| `loc_transaction` | [`LocTransaction`](../../doc/models/loc-transaction.md) | Optional | A line of credit transaction of type |
| `investment_transaction` | [`InvestmentTransaction`](../../doc/models/investment-transaction.md) | Optional | Investment Transactions |
| `insurance_transaction` | [`InsuranceTransaction`](../../doc/models/insurance-transaction.md) | Optional | Insurance transactions |

## Example (as JSON)

```json
{
  "depositTransaction": {
    "accountId": "accountId0",
    "amount": 1.72,
    "category": "category8",
    "debitCreditMemo": "DEBIT",
    "description": "description0"
  },
  "loanTransaction": {
    "accountId": "accountId6",
    "amount": 163.78,
    "category": "category4",
    "debitCreditMemo": "DEBIT",
    "description": "description6"
  },
  "locTransaction": {
    "accountId": "accountId4",
    "amount": 130.76,
    "category": "category2",
    "debitCreditMemo": "DEBIT",
    "description": "description6"
  },
  "investmentTransaction": {
    "accountId": "accountId2",
    "amount": 139.34,
    "category": "category0",
    "debitCreditMemo": "DEBIT",
    "description": "description2"
  },
  "insuranceTransaction": {
    "accountId": "accountId4",
    "amount": 123.56,
    "category": "category2",
    "debitCreditMemo": "DEBIT",
    "description": "description6"
  }
}
```

