
# Debt Security Entity

Information about the debt security specific to the type of security

## Structure

`DebtSecurityEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `par_value` | `float` | Optional | Par value amount |
| `debt_type` | [`DebtTypeEnum`](../../doc/models/debt-type-enum.md) | Optional | Debt type |
| `debt_class` | [`DebtClassEnum`](../../doc/models/debt-class-enum.md) | Optional | Classification of debt |
| `coupon_rate` | `float` | Optional | Bond coupon rate for next closest call date |
| `coupon_date` | `datetime` | Optional | Maturity date for next coupon |
| `coupon_mature_frequency` | [`CouponMatureFrequencyEnum`](../../doc/models/coupon-mature-frequency-enum.md) | Optional | When coupons mature |
| `call_price` | `float` | Optional | Bond call price |
| `yield_to_call` | `float` | Optional | Yield to next call |
| `call_date` | `datetime` | Optional | Next call date |
| `call_type` | [`CallTypeEnum`](../../doc/models/call-type-enum.md) | Optional | Type of next call |
| `yield_to_maturity` | `float` | Optional | Yield to maturity |
| `bond_maturity_date` | `datetime` | Optional | Bond Maturity date |

## Example (as JSON)

```json
{
  "parValue": 18.14,
  "debtType": "ASSET",
  "debtClass": "CORPORATE",
  "couponRate": 229.02,
  "couponDate": "2016-03-13T12:52:32.123Z"
}
```

