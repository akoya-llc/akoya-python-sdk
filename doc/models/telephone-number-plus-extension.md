
# Telephone Number Plus Extension

A telephone number that can contain optional text for an arbitrary length telephone extension number

## Structure

`TelephoneNumberPlusExtension`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`TelephoneNumberTypeEnum`](../../doc/models/telephone-number-type-enum.md) | Optional | Type of phone number: HOME, BUSINESS, CELL, FAX |
| `country` | [`ISO3166CountryCodeEnum`](../../doc/models/iso3166-country-code-enum.md) | Optional | Country calling codes defined by ITU-T recommendations E.123 and E.164 |
| `number` | `str` | Optional | Telephone subscriber number defined by ITU-T recommendation E.164<br><br>**Constraints**: *Maximum Length*: `15`, *Pattern*: `\d+` |
| `extension` | `str` | Optional | An arbitrary length telephone number extension |

## Example (as JSON)

```json
{
  "type": "FAX",
  "country": "GG",
  "number": "number6",
  "extension": "extension4"
}
```

