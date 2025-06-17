
# Account Contact Entity

Contact information for the account

## Structure

`AccountContactEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `holders` | [`List[AccountHolderEntity]`](../../doc/models/account-holder-entity.md) | Optional | Owners of the account |
| `emails` | `List[str]` | Optional | Email addresses associated with the account |
| `addresses` | [`List[DeliveryAddress]`](../../doc/models/delivery-address.md) | Optional | - |
| `telephones` | [`List[TelephoneNumber]`](../../doc/models/telephone-number.md) | Optional | Telephone numbers associated with the account. |

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
        "suffix": "suffix0"
      },
      "relationship": "PRIMARY"
    },
    {
      "customerId": "customerId0",
      "name": {
        "first": "first6",
        "middle": "middle6",
        "last": "last0",
        "prefix": "prefix8",
        "suffix": "suffix0"
      },
      "relationship": "PRIMARY"
    }
  ],
  "emails": [
    "emails1"
  ],
  "addresses": [
    {
      "line1": "line16",
      "line2": "line28",
      "line3": "line36",
      "city": "city4",
      "state": "state0"
    }
  ],
  "telephones": [
    {
      "type": "FAX",
      "country": "GB",
      "number": "number4"
    },
    {
      "type": "FAX",
      "country": "GB",
      "number": "number4"
    },
    {
      "type": "FAX",
      "country": "GB",
      "number": "number4"
    }
  ]
}
```

