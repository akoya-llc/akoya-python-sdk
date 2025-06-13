
# Address Info

*This model accepts additional fields of type Any.*

## Structure

`AddressInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`LocationType`](../../doc/models/location-type.md) | Optional | The location type of an address |
| `line_1` | `str` | Optional | May contain full address if not separated |
| `line_2` | `str` | Optional | - |
| `line_3` | `str` | Optional | - |
| `city` | `str` | Optional | - |
| `state` | `str` | Optional | - |
| `postal_code` | `str` | Optional | - |
| `country` | `str` | Optional | ISO 3166 Country Code |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "type": "MAILING",
  "line1": "line12",
  "line2": "line24",
  "line3": "line32",
  "city": "city0",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

