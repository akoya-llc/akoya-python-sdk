
# Transactions Entity

Optionally paginated array of transactions

## Structure

`TransactionsEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`Links`](../../doc/models/links.md) | Optional | - |
| `transactions` | List[[DepositTransactionInfo](../../doc/models/deposit-transaction-info.md) \| [LoanTransactionInfo](../../doc/models/loan-transaction-info.md) \| [LocTransactionInfo](../../doc/models/loc-transaction-info.md) \| [InvestmentTransactionInfo](../../doc/models/investment-transaction-info.md) \| [InsuranceTransactionInfo](../../doc/models/insurance-transaction-info.md)] \| None | Optional | This is List of a container for any-of cases. |

## Example (as JSON)

```json
{
  "links": {
    "next": {
      "href": "href4"
    },
    "prev": {
      "href": "href8"
    }
  },
  "transactions": [
    {
      "depositTransaction": {
        "accountId": "accountId0",
        "amount": 1.72,
        "category": "category8",
        "debitCreditMemo": "DEBIT",
        "description": "description0"
      }
    }
  ]
}
```

