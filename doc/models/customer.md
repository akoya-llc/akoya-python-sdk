
# Customer

Represents a customer (end-user)

## Structure

`Customer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Optional | Long-term persistent identity of the end-user. This identity must be unique to the owning institution |
| `name` | [`Name`](../../doc/models/name.md) | Optional | The end-user's name |

## Example (as JSON)

```json
{
  "customerId": "customerId2",
  "name": {
    "first": "first6",
    "middle": "middle6",
    "last": "last0",
    "prefix": "prefix8",
    "suffix": "suffix0"
  }
}
```

