
# Health Insurance Marketplace Covered Individual

Used on Form 1095-A Part II

## Structure

`HealthInsuranceMarketplaceCoveredIndividual`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Covered individual name |
| `tin` | `str` | Optional | Covered individual SSN |
| `date_of_birth` | `date` | Optional | Covered individual date of birth |
| `policy_start_date` | `date` | Optional | Coverage start date |
| `policy_termination_date` | `date` | Optional | Coverage termination date |

## Example (as JSON)

```json
{
  "dateOfBirth": "2021-07-15",
  "policyStartDate": "2021-07-15",
  "policyTerminationDate": "2021-07-15",
  "name": "name2",
  "tin": "tin8"
}
```

