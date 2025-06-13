
# Customer

Represents a customer (end-user)

*This model accepts additional fields of type Any.*

## Structure

`Customer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Optional | Long-term persistent identity of the end-user. This identity must be unique to the owning institution |
| `name` | [`Name`](../../doc/models/name.md) | Optional | The end-user's name |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "customerId": "customerId2",
  "name": {
    "first": "first6",
    "middle": "middle6",
    "last": "last0",
    "prefix": "prefix8",
    "suffix": "suffix0",
    "exampleAdditionalProperty": {
      "key1": "val1",
      "key2": "val2"
    }
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

