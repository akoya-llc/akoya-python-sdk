
# Pension Source Entity

Information about a pension source.

## Structure

`PensionSourceEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_name` | `str` | Optional | Name of the Source |
| `amount` | `float` | Optional | Benefit Amount |
| `payment_option` | `str` | Optional | Form of payment |
| `as_of_date` | `datetime` | Optional | Date benefit was calculated |
| `frequency` | [`FrequencyEnum`](../../doc/models/frequency-enum.md) | Optional | - |
| `start_date` | `datetime` | Optional | Assumed retirement date ‐ As of date amount is payable |

## Example (as JSON)

```json
{
  "displayName": "displayName8",
  "amount": 9.06,
  "paymentOption": "paymentOption0",
  "asOfDate": "2016-03-13T12:52:32.123Z",
  "frequency": "ANNUALLY"
}
```

