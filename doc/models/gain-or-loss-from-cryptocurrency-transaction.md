
# Gain or Loss From Cryptocurrency Transaction

Tax information for a single cryptocurrency transaction. If reported on Form 1099-B, use Tax1099B and SecurityDetail instead of this entity.

## Structure

`GainOrLossFromCryptocurrencyTransaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cryptocurrency_name` | `str` | Optional | Cryptocurrency name (e.g. Bitcoin) |
| `symbol` | `str` | Optional | Cryptocurrency abbreviation or symbol (e.g. BTC) |
| `quantity` | `float` | Optional | Quantity (e.g. 0.0125662) |
| `sale_description` | `str` | Optional | Description of property (1099-B box 1a) |
| `date_acquired` | `date` | Optional | Date acquired (1099-B box 1b) |
| `various_dates_acquired` | `bool` | Optional | Acquired on various dates (1099-B box 1b) |
| `date_of_sale` | `date` | Optional | Date sold or disposed (1099-B box 1c) |
| `sales_price` | `float` | Optional | Proceeds (not price per share, 1099-B box 1d) |
| `cost_basis` | `float` | Optional | Cost or other basis (1099-B box 1e) |
| `long_or_short` | [`SaleTermTypeEnum`](../../doc/models/sale-term-type-enum.md) | Optional | LONG or SHORT (1099-B box 2) |

## Example (as JSON)

```json
{
  "dateAcquired": "2021-07-15",
  "dateOfSale": "2021-07-15",
  "cryptocurrencyName": "cryptocurrencyName6",
  "symbol": "symbol0",
  "quantity": 100.14,
  "saleDescription": "saleDescription2"
}
```

