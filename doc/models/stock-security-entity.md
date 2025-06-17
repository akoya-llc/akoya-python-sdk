
# Stock Security Entity

Information about the stock security specific to the type of security

## Structure

`StockSecurityEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `units_street` | `float` | Optional | Units in the FI's street name, positive quantity |
| `units_user` | `float` | Optional | Units in user's name directly, positive  quantity |
| `reinvest_dividends` | `bool` | Optional | Reinvest dividends |
| `stock_type` | [`StockTypeEnum`](../../doc/models/stock-type-enum.md) | Optional | - |
| `myield` | `float` | Optional | Current yield |
| `yield_as_of_date` | `datetime` | Optional | Yield as-of date |

## Example (as JSON)

```json
{
  "unitsStreet": 117.56,
  "unitsUser": 92.52,
  "reinvestDividends": false,
  "stockType": "STOCK",
  "yield": 211.18
}
```

