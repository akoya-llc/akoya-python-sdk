
# Telephone Number

Standard for international phone numbers

## Structure

`TelephoneNumber`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`TelephoneNumberTypeEnum`](../../doc/models/telephone-number-type-enum.md) | Optional | Type of phone number: HOME, BUSINESS, CELL, FAX |
| `country` | [`ISO3166CountryCodeEnum`](../../doc/models/iso3166-country-code-enum.md) | Optional | Country calling codes defined by ITU-T recommendations E.123 and E.164 |
| `number` | `str` | Optional | Telephone subscriber number defined by ITU-T recommendation E.164<br><br>**Constraints**: *Maximum Length*: `15`, *Pattern*: `\d+` |

## Example (as JSON)

```json
{
  "type": "FAX",
  "country": "CH",
  "number": "number8"
}
```

