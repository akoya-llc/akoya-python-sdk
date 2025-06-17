
# Local Tax Withholding

Income in a locality and its tax withholding

## Structure

`LocalTaxWithholding`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tax_withheld` | `float` | Optional | Amount of local income tax withheld |
| `locality_name` | `str` | Optional | Locality name |
| `income` | `float` | Optional | Income amount for local tax purposes |

## Example (as JSON)

```json
{
  "taxWithheld": 97.82,
  "localityName": "localityName0",
  "income": 162.16
}
```

