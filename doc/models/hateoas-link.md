
# HATEOAS Link

REST application constraint (Hypermedia As The Engine Of Application State)

## Structure

`HATEOASLink`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | URL to invoke the action on the resource |
| `action` | [`HttpMethodEnum`](../../doc/models/http-method-enum.md) | Optional | HTTP Method to use for the request |
| `types` | [`List[ContentTypeEnum]`](../../doc/models/content-type-enum.md) | Optional | Content-types that can be used in the Accept header. |

## Example (as JSON)

```json
{
  "href": "https://api.fi.com/fdx/v4/accounts/12345",
  "action": "DELETE",
  "types": [
    "image/gif"
  ]
}
```

