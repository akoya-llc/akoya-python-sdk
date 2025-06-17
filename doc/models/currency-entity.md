
# Currency Entity

Indicates the currency code used by the account. May also include currency rate.

## Structure

`CurrencyEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Optional | Iso 4217 currency code. |
| `currency_rate` | `float` | Optional | Currency rate between original and converted currency. |
| `original_currency_code` | `str` | Optional | Iso 4217 currency code. |

## Example (as JSON)

```json
{
  "currencyCode": "currencyCode4",
  "currencyRate": 203.06,
  "originalCurrencyCode": "originalCurrencyCode0"
}
```

