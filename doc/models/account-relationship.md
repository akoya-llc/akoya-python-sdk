
# Account Relationship

*This model accepts additional fields of type Any.*

## Structure

`AccountRelationship`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Optional | Account ID of the related account |
| `relationship` | [`RelationshipType`](../../doc/models/relationship-type.md) | Optional | Types of relationships between accounts and holders. Suggested values |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "accountId": "accountId0",
  "relationship": "FOR_BENEFIT_OF",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

