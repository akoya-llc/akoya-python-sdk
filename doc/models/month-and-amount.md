
# Month and Amount

Month and amount pair used on IRS Form 1099-K, etc.

## Structure

`MonthAndAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `month` | [`MonthAbbreviationEnum`](../../doc/models/month-abbreviation-enum.md) | Optional | Month |
| `amount` | `float` | Optional | Amount |

## Example (as JSON)

```json
{
  "month": "SEP",
  "amount": 97.94
}
```

