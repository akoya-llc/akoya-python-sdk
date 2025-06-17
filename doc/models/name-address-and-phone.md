
# Name Address and Phone

Contact phone number with name and address

## Structure

`NameAddressAndPhone`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `line_1` | `str` | Optional | Address line 1 |
| `line_2` | `str` | Optional | Address line 2 |
| `line_3` | `str` | Optional | Address line 3 |
| `city` | `str` | Optional | City |
| `state` | `str` | Optional | State |
| `region` | `str` | Optional | State, Province, Territory, Canton or Prefecture. From [Universal Postal Union](https://www.upu.int/en/Postal-Solutions/Programmes-Services/Addressing-Solutions#addressing-s42-standard) as of 2-26-2020, [S42 International Address Standards](https://www.upu.int/UPU/media/upu/documents/PostCode/S42_International-Addressing-Standards.pdf). For U.S. addresses can be 2-character code from '#/components/schemas/StateCode' |
| `postal_code` | `str` | Optional | Postal code<br><br>**Constraints**: *Maximum Length*: `16` |
| `country` | [`ISO3166CountryCode4Enum`](../../doc/models/iso3166-country-code-4-enum.md) | Optional | Country code |
| `name_1` | `str` | Optional | Name line 1 |
| `name_2` | `str` | Optional | Name line 2 |
| `phone` | [`TelephoneNumberPlusExtension`](../../doc/models/telephone-number-plus-extension.md) | Optional | A telephone number that can contain optional text for an arbitrary length telephone extension number |

## Example (as JSON)

```json
{
  "country": "US",
  "line1": "line16",
  "line2": "line28",
  "line3": "line36",
  "city": "city4",
  "state": "state0"
}
```

