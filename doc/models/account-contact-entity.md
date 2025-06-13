
# Account Contact Entity

Contact information for the account

*This model accepts additional fields of type Any.*

## Structure

`AccountContactEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `holders` | [`List[AccountHolderEntity]`](../../doc/models/account-holder-entity.md) | Optional | Owners of the account |
| `emails` | `List[str]` | Optional | Email addresses associated with the account |
| `addresses` | [`List[DeliveryAddressDetails]`](../../doc/models/delivery-address-details.md) | Optional | - |
| `telephones` | [`List[TelephoneNumber]`](../../doc/models/telephone-number.md) | Optional | Telephone numbers associated with the account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "holders": [
    {
      "customerId": "customerId0",
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
      "relationship": "FOR_BENEFIT_OF_SECONDARY_JOINT_RESTRICTED",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "customerId": "customerId0",
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
      "relationship": "FOR_BENEFIT_OF_SECONDARY_JOINT_RESTRICTED",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "emails": [
    "emails1"
  ],
  "addresses": [
    {
      "type": "type6",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "telephones": [
    {
      "type": "FAX",
      "country": "country0",
      "number": "number4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "type": "FAX",
      "country": "country0",
      "number": "number4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    },
    {
      "type": "FAX",
      "country": "country0",
      "number": "number4",
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

