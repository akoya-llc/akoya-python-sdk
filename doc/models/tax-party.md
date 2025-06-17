
# Tax Party

Legal entity for issuer or recipient, used across all tax forms

## Structure

`TaxParty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tin` | `str` | Optional | Issuer or recipient Tax Identification Number. Usually EIN for issuer and SSN for recipient |
| `party_type` | [`TaxPartyTypeEnum`](../../doc/models/tax-party-type-enum.md) | Optional | Type of issuer or recipient legal entity, as "BUSINESS" or "INDIVIDUAL". Commonly BUSINESS for issuer and INDIVIDUAL for recipient |
| `individual_name` | [`IndividualName`](../../doc/models/individual-name.md) | Optional | Individual issuer or recipient name |
| `business_name` | [`BusinessName`](../../doc/models/business-name.md) | Optional | Business issuer or recipient name |
| `address` | [`Address`](../../doc/models/address.md) | Optional | Issuer or recipient address |
| `phone` | [`TelephoneNumberPlusExtension`](../../doc/models/telephone-number-plus-extension.md) | Optional | Issuer or recipient telephone number |
| `email` | `str` | Optional | Issuer or recipient email address. (Additional information, not part of IRS forms) |

## Example (as JSON)

```json
{
  "tin": "tin6",
  "partyType": "BUSINESS",
  "individualName": {
    "first": "first0",
    "middle": "middle0",
    "last": "last4",
    "suffix": "suffix4"
  },
  "businessName": {
    "name1": "name18",
    "name2": "name22"
  },
  "address": {
    "line1": "line18",
    "line2": "line20",
    "line3": "line38",
    "city": "city6",
    "state": "state2"
  }
}
```

