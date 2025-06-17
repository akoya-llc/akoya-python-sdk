
# Address Info

## Structure

`AddressInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`LocationTypeEnum`](../../doc/models/location-type-enum.md) | Optional | The location type of an address |
| `line_1` | `str` | Optional | May contain full address if not separated |
| `line_2` | `str` | Optional | - |
| `line_3` | `str` | Optional | - |
| `city` | `str` | Optional | - |
| `state` | `str` | Optional | - |
| `postal_code` | `str` | Optional | - |
| `country` | `str` | Optional | ISO 3166 Country Code |

## Example (as JSON)

```json
{
  "type": "MAILING",
  "line1": "line12",
  "line2": "line24",
  "line3": "line32",
  "city": "city0"
}
```

