
# Vesting Entity

Provides the past, present, and future vesting schedule and percentages.

## Structure

`VestingEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vesting_date` | `datetime` | Optional | Vesting date |
| `symbol` | `str` | Optional | Security symbol |
| `strike_price` | `float` | Optional | Strike price |
| `vesting_percentage` | `float` | Optional | Vesting percentage |
| `other_vest_amount` | `float` | Optional | Other vest amount |
| `other_vest_percentage` | `float` | Optional | Other vest percentage |
| `vested_balance` | `float` | Optional | Vested balance |
| `un_vested_balance` | `float` | Optional | Unvested balance |
| `vested_quantity` | `float` | Optional | Vested qualtity |
| `un_vested_quantity` | `float` | Optional | Unvested quantity |

## Example (as JSON)

```json
{
  "vestingDate": "2016-03-13T12:52:32.123Z",
  "symbol": "symbol0",
  "strikePrice": 216.86,
  "vestingPercentage": 250.28,
  "otherVestAmount": 111.28
}
```

