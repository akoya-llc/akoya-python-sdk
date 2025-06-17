
# Form 1099 INT

Interest Income

## Structure

`Form1099INT`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tax_year` | `int` | Optional | Year for which taxes are being paid<br><br>**Constraints**: `>= 2018`, `<= 2050` |
| `corrected` | `bool` | Optional | True to indicate this is a corrected tax form |
| `account_id` | `str` | Optional | Long-term persistent identity of the source account. Not the account number |
| `tax_form_id` | `str` | Optional | Long-term persistent id for this tax form. Depending upon the data provider, this may be the same id as the enclosing tax statement id, or this may be a different id, or this id may be omitted. |
| `tax_form_date` | `date` | Optional | Date of production or delivery of the tax form |
| `additional_information` | `str` | Optional | Additional explanation text or content about this tax form |
| `tax_form_type` | [`TypeFormTypeEnum`](../../doc/models/type-form-type-enum.md) | Optional | Enumerated name of the tax form entity e.g. "TaxW2" |
| `issuer` | [`TaxParty`](../../doc/models/tax-party.md) | Optional | Issuer's name, address, phone, and TIN. Issuer data need only be transmitted on enclosing TaxStatement, if it is the same on all its included tax forms. |
| `recipient` | [`TaxParty`](../../doc/models/tax-party.md) | Optional | Recipient's name, address, phone, and TIN. Recipient data need only be transmitted on enclosing TaxStatement, if it is the same on all its included tax forms. |
| `attributes` | [`List[TaxFormAttribute]`](../../doc/models/tax-form-attribute.md) | Optional | Additional attributes for this tax form when defined fields are not available. Some specific additional attributes already defined by providers: Fields required by [IRS FIRE](https://www.irs.gov/e-file-providers/filing-information-returns-electronically-fire): Name Control, Type of Identification Number (EIN, SSN, ITIN, ATIN). (ATIN is tax ID number for pending adoptions.) Tax form provider field for taxpayer notification: Recipient Email Address. |
| `error` | [`Error`](../../doc/models/error.md) | Optional | Present if an error was encountered while retrieving this form |
| `links` | [`List[HATEOASLink]`](../../doc/models/hateoas-link.md) | Optional | Links to retrieve this form as data or image, or to invoke other APIs |
| `foreign_account_tax_compliance` | `bool` | Optional | FATCA filing requirement |
| `account_number` | `str` | Optional | Account number |
| `payer_rtn` | `str` | Optional | Payer's RTN |
| `interest_income` | `float` | Optional | Box 1, Interest income |
| `early_withdrawal_penalty` | `float` | Optional | Box 2, Early withdrawal penalty |
| `us_bond_interest` | `float` | Optional | Box 3, Interest on U.S. Savings Bonds and Treasury obligations |
| `federal_tax_withheld` | `float` | Optional | Box 4, Federal income tax withheld |
| `investment_expenses` | `float` | Optional | Box 5, Investment expenses |
| `foreign_tax_paid` | `float` | Optional | Box 6, Foreign tax paid |
| `foreign_country` | `str` | Optional | Box 7, Foreign country or U.S. possession |
| `tax_exempt_interest` | `float` | Optional | Box 8, Tax-exempt interest |
| `specified_pab_interest` | `float` | Optional | Box 9, Specified private activity bond interest |
| `market_discount` | `float` | Optional | Box 10, Market discount |
| `bond_premium` | `float` | Optional | Box 11, Bond premium |
| `us_bond_premium` | `float` | Optional | Box 12, Bond premium on Treasury obligations |
| `tax_exempt_bond_premium` | `float` | Optional | Box 13, Bond premium on tax-exempt bond |
| `cusip_number` | `str` | Optional | Box 14, Tax-exempt bond CUSIP no. |
| `state_and_local` | [`List[StateAndLocalTaxWithholding]`](../../doc/models/state-and-local-tax-withholding.md) | Optional | Boxes 15-17, State and Local tax withholding |
| `foreign_incomes` | [`List[DescriptionAndAmount]`](../../doc/models/description-and-amount.md) | Optional | Supplemental foreign income amount information (description is country) |
| `state_tax_exempt_income` | [`List[DescriptionAndAmount]`](../../doc/models/description-and-amount.md) | Optional | Supplemental tax-exempt income by state (description is state) |
| `second_tin_notice` | `bool` | Optional | Second TIN Notice |

## Example (as JSON)

```json
{
  "taxYear": 2023,
  "taxFormDate": "2021-07-15",
  "attributes": [
    {
      "name": "nameControl",
      "value": "WILC"
    },
    {
      "name": "recipientIdType",
      "value": "EIN",
      "code": "1"
    },
    {
      "name": "recipientIdType",
      "value": "SSN",
      "code": "2"
    },
    {
      "name": "recipientIdType",
      "value": "ITIN",
      "code": "2"
    },
    {
      "name": "recipientIdType",
      "value": "ATIN",
      "code": "2"
    }
  ],
  "corrected": false,
  "accountId": "accountId2",
  "taxFormId": "taxFormId0"
}
```

