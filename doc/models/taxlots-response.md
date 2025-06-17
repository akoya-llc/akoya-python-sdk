
# Taxlots Response

## Structure

`TaxlotsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Optional | Corresponds to AccountId in Account |
| `holding` | [`Holding`](../../doc/models/holding.md) | Optional | - |

## Example (as JSON)

```json
{
  "accountId": "accountId6",
  "holding": {
    "holdingId": "holdingId0",
    "securityId": "securityId2",
    "securityIdType": "VALOR",
    "taxLots": [
      {
        "costBasis": 131.38,
        "currentValue": 199.34,
        "originalPurchaseDate": "2016-03-13T12:52:32.123Z",
        "positionType": "LONG",
        "purchasedPrice": 176.16
      },
      {
        "costBasis": 131.38,
        "currentValue": 199.34,
        "originalPurchaseDate": "2016-03-13T12:52:32.123Z",
        "positionType": "LONG",
        "purchasedPrice": 176.16
      },
      {
        "costBasis": 131.38,
        "currentValue": 199.34,
        "originalPurchaseDate": "2016-03-13T12:52:32.123Z",
        "positionType": "LONG",
        "purchasedPrice": 176.16
      }
    ]
  }
}
```

