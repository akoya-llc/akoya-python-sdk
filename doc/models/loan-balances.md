
# Loan Balances

Data elements included with balances specific to loan accounts

## Structure

`LoanBalances`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Optional | Long-term persistent identity of the account. Not an account number. This identity must be unique to the owning institution. |
| `account_type` | `str` | Optional | The type of an account. For instance, CHECKING, SAVINGS, 401K, etc. |
| `account_number_display` | `str` | Optional | Account display number for the end user’s handle at owning institution. This is to be displayed by the Interface Provider. |
| `currency` | [`CurrencyEntity`](../../doc/models/currency-entity.md) | Optional | Indicates the currency code used by the account. May also include currency rate. |
| `description` | `str` | Optional | - |
| `fi_attributes` | [`List[FiAttributeEntity]`](../../doc/models/fi-attribute-entity.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `nickname` | `str` | Optional | Name given by the user. Used in UIs to assist in account selection |
| `product_name` | `str` | Optional | Marketed product name for this account.  Used in UIs to assist in account selection |
| `status` | [`AccountInfoStatusEnum`](../../doc/models/account-info-status-enum.md) | Optional | The status of an account. |
| `line_of_business` | `str` | Optional | The line of business, such as consumer, consumer joint, small business, corporate, etc. |
| `balance_type` | [`BalanceTypeEnum`](../../doc/models/balance-type-enum.md) | Optional | ASSET (positive transaction amount increases balance), LIABILITY (positive transaction amount decreases balance) |
| `interest_rate` | `float` | Optional | Interest Rate of Account |
| `interest_rate_type` | [`InterestRateTypeEnum`](../../doc/models/interest-rate-type-enum.md) | Optional | The type of interest rate. FIXED or VARIABLE. |
| `interest_rate_as_of` | `datetime` | Optional | Date of account’s interest rate |
| `last_activity_date` | `datetime` | Optional | Date that last transaction occurred on account |
| `micr_number` | `str` | Optional | MICR Number |
| `parent_account_id` | `str` | Optional | Long-term persistent identity of the parent account. This is used to group accounts. |
| `prior_interest_rate` | `float` | Optional | Previous Interest Rate of Account |
| `transfer_in` | `bool` | Optional | Account is eligible for incoming transfers |
| `transfer_out` | `bool` | Optional | Account is eligible for outgoing transfers |
| `compounding_period` | [`CompoundingPeriodEnum`](../../doc/models/compounding-period-enum.md) | Optional | - |
| `loan_term` | `int` | Optional | Term of loan in months |
| `maturity_date` | `datetime` | Optional | Maturity date |
| `originating_date` | `datetime` | Optional | Loan origination date |
| `payment_frequency` | [`LoanAccountPaymentFrequencyEnum`](../../doc/models/loan-account-payment-frequency-enum.md) | Optional | - |
| `total_number_of_payments` | `int` | Optional | Total number of payments |
| `balance_as_of` | `datetime` | Optional | As-of date of balances |
| `escrow_balance` | `float` | Optional | Escrow balance of loan |
| `interest_paid_year_to_date` | `float` | Optional | Interest paid year to date |
| `last_payment_amount` | `float` | Optional | Last payment amount |
| `last_payment_date` | `datetime` | Optional | Last payment date |
| `next_payment_amount` | `float` | Optional | Amount of next payment |
| `next_payment_date` | `datetime` | Optional | Date of next payment |
| `original_principal` | `float` | Optional | Original principal of loan |
| `pay_off_amount` | `float` | Optional | Payoff amount |
| `principal_balance` | `float` | Optional | Principal balance of loan |

## Example (as JSON)

```json
{
  "accountId": "accountId8",
  "accountType": "accountType8",
  "accountNumberDisplay": "accountNumberDisplay4",
  "currency": {
    "currencyCode": "currencyCode0",
    "currencyRate": 27.48,
    "originalCurrencyCode": "originalCurrencyCode4"
  },
  "description": "description8"
}
```

