
# Telephone Number

Standard for international phone numbers

*This model accepts additional fields of type Any.*

## Structure

`TelephoneNumber`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`TelephoneNumberType`](../../doc/models/telephone-number-type.md) | Optional | Type of phone number: HOME, BUSINESS, CELL, FAX |
| `country` | `str` | Optional | Country calling codes defined by ITU-T recommendations E.123 and E.164<br><br>**Constraints**: *Maximum Length*: `3` |
| `number` | `str` | Optional | Telephone subscriber number defined by ITU-T recommendation E.164<br><br>**Constraints**: *Maximum Length*: `15`, *Pattern*: `\d+` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "type": "FAX",
  "country": "country8",
  "number": "number8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

