
# Investment Balance List

## Structure

`InvestmentBalanceList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_name` | `str` | Optional | Name of the balance. |
| `balance_description` | `str` | Optional | Description of balance. |
| `balance_type` | [`InvestmentBalanceTypeEnum`](../../doc/models/investment-balance-type-enum.md) | Optional | The type of an investment balance. AMOUNT or PERCENTAGE. |
| `balance_value` | `float` | Optional | Value of balance name. |
| `balance_date` | `datetime` | Optional | Date as of this balance. |
| `currency` | [`CurrencyEntity`](../../doc/models/currency-entity.md) | Optional | Indicates the currency code used by the account. May also include currency rate. |

## Example (as JSON)

```json
{
  "balanceName": "balanceName0",
  "balanceDescription": "balanceDescription6",
  "balanceType": "AMOUNT",
  "balanceValue": 220.9,
  "balanceDate": "2016-03-13T12:52:32.123Z"
}
```

