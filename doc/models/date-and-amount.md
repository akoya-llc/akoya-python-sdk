
# Date and Amount

Date, description, and amount. When used in 1098-Q, description is optional

## Structure

`DateAndAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date` | `date` | Optional | Date of amount. When used in 1098-Q, date of last payment in month |
| `description` | `str` | Optional | Description of amount. When used in 1098-Q, may use MonthAbbreviation |
| `amount` | `float` | Optional | Amount of payment or receipt. When used in 1098-Q, monthly total |

## Example (as JSON)

```json
{
  "date": "2021-07-15",
  "description": "description4",
  "amount": 231.46
}
```

