
# Business Customer Entity

Customers that are commercial in nature are affiliated with a business entity

## Structure

`BusinessCustomerEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of business customer |
| `registered_agents` | [`List[CustomerName]`](../../doc/models/customer-name.md) | Optional | A list of registered agents who act on behalf of the business customer |
| `registered_id` | `str` | Optional | The registered tax identification number (TIN) or other identifier of business customer |
| `industry_code` | [`IndustryCode`](../../doc/models/industry-code.md) | Optional | Industry code and type |
| `domicile` | [`Domicile`](../../doc/models/domicile.md) | Optional | The country and region of the business customer's location |

## Example (as JSON)

```json
{
  "name": "name0",
  "registeredAgents": [
    {
      "first": "first6",
      "middle": "middle6",
      "last": "last0",
      "prefix": "prefix8",
      "suffix": "suffix0"
    }
  ],
  "registeredId": "registeredId6",
  "industryCode": {
    "type": "type8",
    "code": "code0"
  },
  "domicile": {
    "region": "region2",
    "country": "country0"
  }
}
```

