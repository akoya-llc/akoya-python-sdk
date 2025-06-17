
# Line Item

## Structure

`LineItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `float` | Optional | The amount of money attributable to this line item |
| `check_number` | `float` | Optional | Check number |
| `description` | `str` | Optional | The description of the line item |
| `image_ids` | `List[str]` | Optional | Array of image identifiers (unique to transaction) used to retrieve images of check or transaction receipt. |
| `links` | [`List[HATEOASLink]`](../../doc/models/hateoas-link.md) | Optional | Links (unique to this Transaction) used to retrieve images of checks or transaction receipts, or invoke other APIs |
| `memo` | `str` | Optional | Secondary item description |
| `reference` | `str` | Optional | A reference number |

## Example (as JSON)

```json
{
  "amount": 197.28,
  "checkNumber": 134.12,
  "description": "description6",
  "imageIds": [
    "imageIds5",
    "imageIds6",
    "imageIds7"
  ],
  "links": [
    {
      "href": "href6",
      "action": "PATCH",
      "types": [
        "application/json",
        "application/pdf"
      ]
    },
    {
      "href": "href6",
      "action": "PATCH",
      "types": [
        "application/json",
        "application/pdf"
      ]
    },
    {
      "href": "href6",
      "action": "PATCH",
      "types": [
        "application/json",
        "application/pdf"
      ]
    }
  ]
}
```

