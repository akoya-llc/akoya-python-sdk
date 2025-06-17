
# Open Order Entity

Information on an open order.

## Structure

`OpenOrderEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `str` | Optional | Long term persistent identity of the order. Id for this order transaction. |
| `security_id` | `str` | Optional | Unique identifier of the security. |
| `security_id_type` | [`SecurityIdTypeEnum`](../../doc/models/security-id-type-enum.md) | Optional | Security identifier type |
| `symbol` | `str` | Optional | Market symbol |
| `description` | `str` | Optional | Description of order |
| `units` | `float` | Optional | Number of units (shares, bonds, etc.) |
| `order_type` | [`OrderTypeEnum`](../../doc/models/order-type-enum.md) | Optional | Type of order. |
| `order_date` | `datetime` | Optional | Order date |
| `unit_price` | `float` | Optional | Unit price |
| `unit_type` | [`UnitTypeEnum`](../../doc/models/unit-type-enum.md) | Optional | Type of unit. |
| `order_duration` | [`OrderDurationEnum`](../../doc/models/order-duration-enum.md) | Optional | This order is good for DAY, GOODTILLCANCEL, IMMEDIATE |
| `sub_account` | [`SubAccountEnum`](../../doc/models/sub-account-enum.md) | Optional | - |
| `limit_price` | `float` | Optional | Limit Price |
| `stop_price` | `float` | Optional | Stop price |
| `inv_401_k_source` | [`Inv401kSourceEnum`](../../doc/models/inv-401-k-source-enum.md) | Optional | For 401(k) accounts, source of money for this order. Default if not present is OTHERNONVEST. |

## Example (as JSON)

```json
{
  "orderId": "orderId4",
  "securityId": "securityId6",
  "securityIdType": "VALOR",
  "symbol": "symbol0",
  "description": "description2"
}
```

