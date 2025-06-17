
# Name

The end-user's name

## Structure

`Name`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first` | `str` | Optional | First or given name. This data element may contain first & last name if not separated. |
| `middle` | `str` | Optional | - |
| `last` | `str` | Optional | - |
| `prefix` | `str` | Optional | Name prefix, e.g. Mr. |
| `suffix` | `str` | Optional | Generational or academic suffix |
| `company` | `str` | Optional | Company name |
| `addresses` | [`List[AddressInfo]`](../../doc/models/address-info.md) | Optional | An array of the end-user's physical mail addresses<br><br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `telephones` | [`List[Telephone]`](../../doc/models/telephone.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `email` | `List[str]` | Optional | An array of the end-user's electronic mail addresses |
| `accounts` | [`List[AccountRelationship]`](../../doc/models/account-relationship.md) | Optional | List of accounts related to this end-user<br><br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "first": "first6",
  "middle": "middle6",
  "last": "last0",
  "prefix": "prefix8",
  "suffix": "suffix0"
}
```

