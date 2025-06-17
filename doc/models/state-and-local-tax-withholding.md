
# State and Local Tax Withholding

Income in a state and/or locality and its or their tax withholding

## Structure

`StateAndLocalTaxWithholding`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `state_code` | [`StateCodeEnum`](../../doc/models/state-code-enum.md) | Optional | State two-digit code |
| `state` | [`StateTaxWithholding`](../../doc/models/state-tax-withholding.md) | Optional | Amount of state income tax withheld |
| `local` | [`LocalTaxWithholding1`](../../doc/models/local-tax-withholding-1.md) | Optional | Amount of local income tax withheld, if any |

## Example (as JSON)

```json
{
  "stateCode": "IL",
  "state": {
    "taxWithheld": 128.78,
    "taxId": "taxId0",
    "income": 191.56
  },
  "local": {
    "taxWithheld": 75.84,
    "localityName": "localityName6",
    "income": 244.5
  }
}
```

