
# Telephone

*This model accepts additional fields of type Any.*

## Structure

`Telephone`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `str` | Optional | - |
| `mtype` | [`PhoneType`](../../doc/models/phone-type.md) | Optional | - |
| `country` | `str` | Optional | Country calling codes defined by ITU-T recommendations E.123 and E.164 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "number": "number2",
  "type": "CELL",
  "country": "country8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

