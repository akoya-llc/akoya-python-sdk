
# Option Security Entity

Information about the option security specific to the type of security

## Structure

`OptionSecurityEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `secured` | [`SecuredEnum`](../../doc/models/secured-enum.md) | Optional | How the option is secured |
| `option_type` | [`OptionTypeEnum`](../../doc/models/option-type-enum.md) | Optional | - |
| `strike_price` | `float` | Optional | Strike price / Unit price |
| `expire_date` | `datetime` | Optional | Expiration date of option |
| `shares_per_contract` | `float` | Optional | Shares per contract |

## Example (as JSON)

```json
{
  "secured": "COVERED",
  "optionType": "CALL",
  "strikePrice": 0.6,
  "expireDate": "2016-03-13T12:52:32.123Z",
  "sharesPerContract": 217.4
}
```

