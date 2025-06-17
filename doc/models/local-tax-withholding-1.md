
# Local Tax Withholding 1

Amount of local income tax withheld, if any

## Structure

`LocalTaxWithholding1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tax_withheld` | `float` | Optional | Amount of local income tax withheld |
| `locality_name` | `str` | Optional | Locality name |
| `income` | `float` | Optional | Income amount for local tax purposes |

## Example (as JSON)

```json
{
  "taxWithheld": 15.4,
  "localityName": "localityName2",
  "income": 207.06
}
```

