
# Vesting

## Structure

`Vesting`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `vested_quantity` | `float` | Optional | Vested quantity (Vested shares total qty of vesting tranche) |
| `vested_value` | `float` | Optional | Vested balance at grant (aggregate of all vestings) |
| `vesting_date` | `datetime` | Optional | - |
| `vest_expire_date` | `datetime` | Optional | - |
| `vested_status` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "vestedQuantity": 86.14,
  "vestedValue": 183.4,
  "vestingDate": "2016-03-13T12:52:32.123Z",
  "vestExpireDate": "2016-03-13T12:52:32.123Z",
  "vestedStatus": "vestedStatus6"
}
```

