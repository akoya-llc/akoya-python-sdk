
# Account Relationship

## Structure

`AccountRelationship`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Optional | Account ID of the related account |
| `relationship` | [`RelationshipTypeEnum`](../../doc/models/relationship-type-enum.md) | Optional | Types of relationships between accounts and holders. Suggested values |

## Example (as JSON)

```json
{
  "accountId": "accountId0",
  "relationship": "FOR_BENEFIT_OF"
}
```

