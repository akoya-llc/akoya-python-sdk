
# Health Insurance Coverage

Used on Form 1095-A Part III

## Structure

`HealthInsuranceCoverage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enrollment_premium` | `float` | Optional | Monthly enrollment premiums |
| `slcsp_premium` | `float` | Optional | Monthly second lowest cost silver plan (SLCSP) premium |
| `advance_premium_tax_credit_payment` | `float` | Optional | Monthly advance payment of premium tax credit |
| `month` | [`CoverageMonthEnum`](../../doc/models/coverage-month-enum.md) | Optional | Month of coverage |

## Example (as JSON)

```json
{
  "enrollmentPremium": 139.74,
  "slcspPremium": 163.34,
  "advancePremiumTaxCreditPayment": 197.06,
  "month": "MAY"
}
```

