
# Array of Account Payment Networks

An optionally paginated array of payment networks supported by the account

## Structure

`ArrayOfAccountPaymentNetworks`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_networks` | [`List[PaymentNetworkSupportedByAccount]`](../../doc/models/payment-network-supported-by-account.md) | Optional | Array of payment networks |

## Example (as JSON)

```json
{
  "paymentNetworks": [
    {
      "bankId": "bankId0",
      "identifier": "identifier2",
      "identifierType": "identifierType4",
      "type": "type0",
      "transferIn": false
    },
    {
      "bankId": "bankId0",
      "identifier": "identifier2",
      "identifierType": "identifierType4",
      "type": "type0",
      "transferIn": false
    },
    {
      "bankId": "bankId0",
      "identifier": "identifier2",
      "identifierType": "identifierType4",
      "type": "type0",
      "transferIn": false
    }
  ]
}
```

