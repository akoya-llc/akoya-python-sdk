
# Tax Statement List

Tax statement list containing one or more tax statements

## Structure

`TaxStatementList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statements` | [`List[TaxStatement]`](../../doc/models/tax-statement.md) | Optional | The list of tax statements |

## Example (as JSON)

```json
{
  "statements": [
    {
      "taxYear": 2018,
      "taxStatementId": "taxStatementId2",
      "issuer": {
        "tin": "tin0",
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
      },
      "recipient": {
        "tin": "tin2",
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
      },
      "taxDataType": "BASE64_PDF"
    }
  ]
}
```

