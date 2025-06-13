
# Account Holder Entity

Extends `Customer` and adds a `relationship` field to define the customer's relationship with an account

*This model accepts additional fields of type Any.*

## Structure

`AccountHolderEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `str` | Optional | Long-term persistent identity of the end-user. This identity must be unique to the owning institution |
| `name` | [`Name`](../../doc/models/name.md) | Optional | The end-user's name |
| `relationship` | [`AccountHolderRelationship`](../../doc/models/account-holder-relationship.md) | Optional | Customer's relationship to the account |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "customerId": "customerId4",
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
  "relationship": "TRUSTEE",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

