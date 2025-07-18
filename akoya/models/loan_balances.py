# -*- coding: utf-8 -*-

"""
akoya

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from akoya.api_helper import APIHelper
from akoya.models.currency_entity import CurrencyEntity
from akoya.models.fi_attribute_entity import FiAttributeEntity


class LoanBalances(object):

    """Implementation of the 'Loan balances' model.

    Data elements included with balances specific to loan accounts

    Attributes:
        account_id (str): Long-term persistent identity of the account. Not an
            account number. This identity must be unique to the owning
            institution.
        account_type (str): The type of an account. For instance, CHECKING,
            SAVINGS, 401K, etc.
        account_number_display (str): Account display number for the end
            user’s handle at owning institution. This is to be displayed by
            the Interface Provider.
        currency (CurrencyEntity): Indicates the currency code used by the
            account. May also include currency rate.
        description (str): The model property of type str.
        fi_attributes (List[FiAttributeEntity]): The model property of type
            List[FiAttributeEntity].
        nickname (str): Name given by the user. Used in UIs to assist in
            account selection
        product_name (str): Marketed product name for this account.  Used in
            UIs to assist in account selection
        status (AccountInfoStatus): The status of an account.
        line_of_business (str): The line of business, such as consumer,
            consumer joint, small business, corporate, etc.
        balance_type (BalanceType): ASSET (positive transaction amount
            increases balance), LIABILITY (positive transaction amount
            decreases balance)
        interest_rate (float): Interest Rate of Account
        interest_rate_type (InterestRateType): The type of interest rate.
            FIXED or VARIABLE.
        interest_rate_as_of (datetime): Date of account’s interest rate
        last_activity_date (datetime): Date that last transaction occurred on
            account
        micr_number (str): MICR Number
        parent_account_id (str): Long-term persistent identity of the parent
            account. This is used to group accounts.
        prior_interest_rate (float): Previous Interest Rate of Account
        transfer_in (bool): Account is eligible for incoming transfers
        transfer_out (bool): Account is eligible for outgoing transfers
        compounding_period (CompoundingPeriod): The model property of type
            CompoundingPeriod.
        loan_term (int): Term of loan in months
        maturity_date (datetime): Maturity date
        originating_date (datetime): Loan origination date
        payment_frequency (LoanAccountPaymentFrequency): The model property of
            type LoanAccountPaymentFrequency.
        total_number_of_payments (int): Total number of payments
        balance_as_of (datetime): As-of date of balances
        escrow_balance (float): Escrow balance of loan
        interest_paid_year_to_date (float): Interest paid year to date
        last_payment_amount (float): Last payment amount
        last_payment_date (datetime): Last payment date
        next_payment_amount (float): Amount of next payment
        next_payment_date (datetime): Date of next payment
        original_principal (float): Original principal of loan
        pay_off_amount (float): Payoff amount
        principal_balance (float): Principal balance of loan
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id": 'accountId',
        "account_type": 'accountType',
        "account_number_display": 'accountNumberDisplay',
        "currency": 'currency',
        "description": 'description',
        "fi_attributes": 'fiAttributes',
        "nickname": 'nickname',
        "product_name": 'productName',
        "status": 'status',
        "line_of_business": 'lineOfBusiness',
        "balance_type": 'balanceType',
        "interest_rate": 'interestRate',
        "interest_rate_type": 'interestRateType',
        "interest_rate_as_of": 'interestRateAsOf',
        "last_activity_date": 'lastActivityDate',
        "micr_number": 'micrNumber',
        "parent_account_id": 'parentAccountId',
        "prior_interest_rate": 'priorInterestRate',
        "transfer_in": 'transferIn',
        "transfer_out": 'transferOut',
        "compounding_period": 'compoundingPeriod',
        "loan_term": 'loanTerm',
        "maturity_date": 'maturityDate',
        "originating_date": 'originatingDate',
        "payment_frequency": 'paymentFrequency',
        "total_number_of_payments": 'totalNumberOfPayments',
        "balance_as_of": 'balanceAsOf',
        "escrow_balance": 'escrowBalance',
        "interest_paid_year_to_date": 'interestPaidYearToDate',
        "last_payment_amount": 'lastPaymentAmount',
        "last_payment_date": 'lastPaymentDate',
        "next_payment_amount": 'nextPaymentAmount',
        "next_payment_date": 'nextPaymentDate',
        "original_principal": 'originalPrincipal',
        "pay_off_amount": 'payOffAmount',
        "principal_balance": 'principalBalance'
    }

    _optionals = [
        'account_id',
        'account_type',
        'account_number_display',
        'currency',
        'description',
        'fi_attributes',
        'nickname',
        'product_name',
        'status',
        'line_of_business',
        'balance_type',
        'interest_rate',
        'interest_rate_type',
        'interest_rate_as_of',
        'last_activity_date',
        'micr_number',
        'parent_account_id',
        'prior_interest_rate',
        'transfer_in',
        'transfer_out',
        'compounding_period',
        'loan_term',
        'maturity_date',
        'originating_date',
        'payment_frequency',
        'total_number_of_payments',
        'balance_as_of',
        'escrow_balance',
        'interest_paid_year_to_date',
        'last_payment_amount',
        'last_payment_date',
        'next_payment_amount',
        'next_payment_date',
        'original_principal',
        'pay_off_amount',
        'principal_balance',
    ]

    def __init__(self,
                 account_id=APIHelper.SKIP,
                 account_type=APIHelper.SKIP,
                 account_number_display=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 fi_attributes=APIHelper.SKIP,
                 nickname=APIHelper.SKIP,
                 product_name=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 line_of_business=APIHelper.SKIP,
                 balance_type=APIHelper.SKIP,
                 interest_rate=APIHelper.SKIP,
                 interest_rate_type=APIHelper.SKIP,
                 interest_rate_as_of=APIHelper.SKIP,
                 last_activity_date=APIHelper.SKIP,
                 micr_number=APIHelper.SKIP,
                 parent_account_id=APIHelper.SKIP,
                 prior_interest_rate=APIHelper.SKIP,
                 transfer_in=APIHelper.SKIP,
                 transfer_out=APIHelper.SKIP,
                 compounding_period=APIHelper.SKIP,
                 loan_term=APIHelper.SKIP,
                 maturity_date=APIHelper.SKIP,
                 originating_date=APIHelper.SKIP,
                 payment_frequency=APIHelper.SKIP,
                 total_number_of_payments=APIHelper.SKIP,
                 balance_as_of=APIHelper.SKIP,
                 escrow_balance=APIHelper.SKIP,
                 interest_paid_year_to_date=APIHelper.SKIP,
                 last_payment_amount=APIHelper.SKIP,
                 last_payment_date=APIHelper.SKIP,
                 next_payment_amount=APIHelper.SKIP,
                 next_payment_date=APIHelper.SKIP,
                 original_principal=APIHelper.SKIP,
                 pay_off_amount=APIHelper.SKIP,
                 principal_balance=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the LoanBalances class"""

        # Initialize members of the class
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_type is not APIHelper.SKIP:
            self.account_type = account_type 
        if account_number_display is not APIHelper.SKIP:
            self.account_number_display = account_number_display 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if description is not APIHelper.SKIP:
            self.description = description 
        if fi_attributes is not APIHelper.SKIP:
            self.fi_attributes = fi_attributes 
        if nickname is not APIHelper.SKIP:
            self.nickname = nickname 
        if product_name is not APIHelper.SKIP:
            self.product_name = product_name 
        if status is not APIHelper.SKIP:
            self.status = status 
        if line_of_business is not APIHelper.SKIP:
            self.line_of_business = line_of_business 
        if balance_type is not APIHelper.SKIP:
            self.balance_type = balance_type 
        if interest_rate is not APIHelper.SKIP:
            self.interest_rate = interest_rate 
        if interest_rate_type is not APIHelper.SKIP:
            self.interest_rate_type = interest_rate_type 
        if interest_rate_as_of is not APIHelper.SKIP:
            self.interest_rate_as_of = APIHelper.apply_datetime_converter(interest_rate_as_of, APIHelper.RFC3339DateTime) if interest_rate_as_of else None 
        if last_activity_date is not APIHelper.SKIP:
            self.last_activity_date = APIHelper.apply_datetime_converter(last_activity_date, APIHelper.RFC3339DateTime) if last_activity_date else None 
        if micr_number is not APIHelper.SKIP:
            self.micr_number = micr_number 
        if parent_account_id is not APIHelper.SKIP:
            self.parent_account_id = parent_account_id 
        if prior_interest_rate is not APIHelper.SKIP:
            self.prior_interest_rate = prior_interest_rate 
        if transfer_in is not APIHelper.SKIP:
            self.transfer_in = transfer_in 
        if transfer_out is not APIHelper.SKIP:
            self.transfer_out = transfer_out 
        if compounding_period is not APIHelper.SKIP:
            self.compounding_period = compounding_period 
        if loan_term is not APIHelper.SKIP:
            self.loan_term = loan_term 
        if maturity_date is not APIHelper.SKIP:
            self.maturity_date = APIHelper.apply_datetime_converter(maturity_date, APIHelper.RFC3339DateTime) if maturity_date else None 
        if originating_date is not APIHelper.SKIP:
            self.originating_date = APIHelper.apply_datetime_converter(originating_date, APIHelper.RFC3339DateTime) if originating_date else None 
        if payment_frequency is not APIHelper.SKIP:
            self.payment_frequency = payment_frequency 
        if total_number_of_payments is not APIHelper.SKIP:
            self.total_number_of_payments = total_number_of_payments 
        if balance_as_of is not APIHelper.SKIP:
            self.balance_as_of = APIHelper.apply_datetime_converter(balance_as_of, APIHelper.RFC3339DateTime) if balance_as_of else None 
        if escrow_balance is not APIHelper.SKIP:
            self.escrow_balance = escrow_balance 
        if interest_paid_year_to_date is not APIHelper.SKIP:
            self.interest_paid_year_to_date = interest_paid_year_to_date 
        if last_payment_amount is not APIHelper.SKIP:
            self.last_payment_amount = last_payment_amount 
        if last_payment_date is not APIHelper.SKIP:
            self.last_payment_date = APIHelper.apply_datetime_converter(last_payment_date, APIHelper.RFC3339DateTime) if last_payment_date else None 
        if next_payment_amount is not APIHelper.SKIP:
            self.next_payment_amount = next_payment_amount 
        if next_payment_date is not APIHelper.SKIP:
            self.next_payment_date = APIHelper.apply_datetime_converter(next_payment_date, APIHelper.RFC3339DateTime) if next_payment_date else None 
        if original_principal is not APIHelper.SKIP:
            self.original_principal = original_principal 
        if pay_off_amount is not APIHelper.SKIP:
            self.pay_off_amount = pay_off_amount 
        if principal_balance is not APIHelper.SKIP:
            self.principal_balance = principal_balance 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        account_id = dictionary.get("accountId") if dictionary.get("accountId") else APIHelper.SKIP
        account_type = dictionary.get("accountType") if dictionary.get("accountType") else APIHelper.SKIP
        account_number_display = dictionary.get("accountNumberDisplay") if dictionary.get("accountNumberDisplay") else APIHelper.SKIP
        currency = CurrencyEntity.from_dictionary(dictionary.get('currency')) if 'currency' in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        fi_attributes = None
        if dictionary.get('fiAttributes') is not None:
            fi_attributes = [FiAttributeEntity.from_dictionary(x) for x in dictionary.get('fiAttributes')]
        else:
            fi_attributes = APIHelper.SKIP
        nickname = dictionary.get("nickname") if dictionary.get("nickname") else APIHelper.SKIP
        product_name = dictionary.get("productName") if dictionary.get("productName") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        line_of_business = dictionary.get("lineOfBusiness") if dictionary.get("lineOfBusiness") else APIHelper.SKIP
        balance_type = dictionary.get("balanceType") if dictionary.get("balanceType") else APIHelper.SKIP
        interest_rate = dictionary.get("interestRate") if dictionary.get("interestRate") else APIHelper.SKIP
        interest_rate_type = dictionary.get("interestRateType") if dictionary.get("interestRateType") else APIHelper.SKIP
        interest_rate_as_of = APIHelper.RFC3339DateTime.from_value(dictionary.get("interestRateAsOf")).datetime if dictionary.get("interestRateAsOf") else APIHelper.SKIP
        last_activity_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("lastActivityDate")).datetime if dictionary.get("lastActivityDate") else APIHelper.SKIP
        micr_number = dictionary.get("micrNumber") if dictionary.get("micrNumber") else APIHelper.SKIP
        parent_account_id = dictionary.get("parentAccountId") if dictionary.get("parentAccountId") else APIHelper.SKIP
        prior_interest_rate = dictionary.get("priorInterestRate") if dictionary.get("priorInterestRate") else APIHelper.SKIP
        transfer_in = dictionary.get("transferIn") if "transferIn" in dictionary.keys() else APIHelper.SKIP
        transfer_out = dictionary.get("transferOut") if "transferOut" in dictionary.keys() else APIHelper.SKIP
        compounding_period = dictionary.get("compoundingPeriod") if dictionary.get("compoundingPeriod") else APIHelper.SKIP
        loan_term = dictionary.get("loanTerm") if dictionary.get("loanTerm") else APIHelper.SKIP
        maturity_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("maturityDate")).datetime if dictionary.get("maturityDate") else APIHelper.SKIP
        originating_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("originatingDate")).datetime if dictionary.get("originatingDate") else APIHelper.SKIP
        payment_frequency = dictionary.get("paymentFrequency") if dictionary.get("paymentFrequency") else APIHelper.SKIP
        total_number_of_payments = dictionary.get("totalNumberOfPayments") if dictionary.get("totalNumberOfPayments") else APIHelper.SKIP
        balance_as_of = APIHelper.RFC3339DateTime.from_value(dictionary.get("balanceAsOf")).datetime if dictionary.get("balanceAsOf") else APIHelper.SKIP
        escrow_balance = dictionary.get("escrowBalance") if dictionary.get("escrowBalance") else APIHelper.SKIP
        interest_paid_year_to_date = dictionary.get("interestPaidYearToDate") if dictionary.get("interestPaidYearToDate") else APIHelper.SKIP
        last_payment_amount = dictionary.get("lastPaymentAmount") if dictionary.get("lastPaymentAmount") else APIHelper.SKIP
        last_payment_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("lastPaymentDate")).datetime if dictionary.get("lastPaymentDate") else APIHelper.SKIP
        next_payment_amount = dictionary.get("nextPaymentAmount") if dictionary.get("nextPaymentAmount") else APIHelper.SKIP
        next_payment_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("nextPaymentDate")).datetime if dictionary.get("nextPaymentDate") else APIHelper.SKIP
        original_principal = dictionary.get("originalPrincipal") if dictionary.get("originalPrincipal") else APIHelper.SKIP
        pay_off_amount = dictionary.get("payOffAmount") if dictionary.get("payOffAmount") else APIHelper.SKIP
        principal_balance = dictionary.get("principalBalance") if dictionary.get("principalBalance") else APIHelper.SKIP
        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items() if k not in cls._names.values()},
            unboxing_function=lambda value: value)
        # Return an object of this model
        return cls(account_id,
                   account_type,
                   account_number_display,
                   currency,
                   description,
                   fi_attributes,
                   nickname,
                   product_name,
                   status,
                   line_of_business,
                   balance_type,
                   interest_rate,
                   interest_rate_type,
                   interest_rate_as_of,
                   last_activity_date,
                   micr_number,
                   parent_account_id,
                   prior_interest_rate,
                   transfer_in,
                   transfer_out,
                   compounding_period,
                   loan_term,
                   maturity_date,
                   originating_date,
                   payment_frequency,
                   total_number_of_payments,
                   balance_as_of,
                   escrow_balance,
                   interest_paid_year_to_date,
                   last_payment_amount,
                   last_payment_date,
                   next_payment_amount,
                   next_payment_date,
                   original_principal,
                   pay_off_amount,
                   principal_balance,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!r}, '
                f'account_type={(self.account_type if hasattr(self, "account_type") else None)!r}, '
                f'account_number_display={(self.account_number_display if hasattr(self, "account_number_display") else None)!r}, '
                f'currency={(self.currency if hasattr(self, "currency") else None)!r}, '
                f'description={(self.description if hasattr(self, "description") else None)!r}, '
                f'fi_attributes={(self.fi_attributes if hasattr(self, "fi_attributes") else None)!r}, '
                f'nickname={(self.nickname if hasattr(self, "nickname") else None)!r}, '
                f'product_name={(self.product_name if hasattr(self, "product_name") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'line_of_business={(self.line_of_business if hasattr(self, "line_of_business") else None)!r}, '
                f'balance_type={(self.balance_type if hasattr(self, "balance_type") else None)!r}, '
                f'interest_rate={(self.interest_rate if hasattr(self, "interest_rate") else None)!r}, '
                f'interest_rate_type={(self.interest_rate_type if hasattr(self, "interest_rate_type") else None)!r}, '
                f'interest_rate_as_of={(self.interest_rate_as_of if hasattr(self, "interest_rate_as_of") else None)!r}, '
                f'last_activity_date={(self.last_activity_date if hasattr(self, "last_activity_date") else None)!r}, '
                f'micr_number={(self.micr_number if hasattr(self, "micr_number") else None)!r}, '
                f'parent_account_id={(self.parent_account_id if hasattr(self, "parent_account_id") else None)!r}, '
                f'prior_interest_rate={(self.prior_interest_rate if hasattr(self, "prior_interest_rate") else None)!r}, '
                f'transfer_in={(self.transfer_in if hasattr(self, "transfer_in") else None)!r}, '
                f'transfer_out={(self.transfer_out if hasattr(self, "transfer_out") else None)!r}, '
                f'compounding_period={(self.compounding_period if hasattr(self, "compounding_period") else None)!r}, '
                f'loan_term={(self.loan_term if hasattr(self, "loan_term") else None)!r}, '
                f'maturity_date={(self.maturity_date if hasattr(self, "maturity_date") else None)!r}, '
                f'originating_date={(self.originating_date if hasattr(self, "originating_date") else None)!r}, '
                f'payment_frequency={(self.payment_frequency if hasattr(self, "payment_frequency") else None)!r}, '
                f'total_number_of_payments={(self.total_number_of_payments if hasattr(self, "total_number_of_payments") else None)!r}, '
                f'balance_as_of={(self.balance_as_of if hasattr(self, "balance_as_of") else None)!r}, '
                f'escrow_balance={(self.escrow_balance if hasattr(self, "escrow_balance") else None)!r}, '
                f'interest_paid_year_to_date={(self.interest_paid_year_to_date if hasattr(self, "interest_paid_year_to_date") else None)!r}, '
                f'last_payment_amount={(self.last_payment_amount if hasattr(self, "last_payment_amount") else None)!r}, '
                f'last_payment_date={(self.last_payment_date if hasattr(self, "last_payment_date") else None)!r}, '
                f'next_payment_amount={(self.next_payment_amount if hasattr(self, "next_payment_amount") else None)!r}, '
                f'next_payment_date={(self.next_payment_date if hasattr(self, "next_payment_date") else None)!r}, '
                f'original_principal={(self.original_principal if hasattr(self, "original_principal") else None)!r}, '
                f'pay_off_amount={(self.pay_off_amount if hasattr(self, "pay_off_amount") else None)!r}, '
                f'principal_balance={(self.principal_balance if hasattr(self, "principal_balance") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!s}, '
                f'account_type={(self.account_type if hasattr(self, "account_type") else None)!s}, '
                f'account_number_display={(self.account_number_display if hasattr(self, "account_number_display") else None)!s}, '
                f'currency={(self.currency if hasattr(self, "currency") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s}, '
                f'fi_attributes={(self.fi_attributes if hasattr(self, "fi_attributes") else None)!s}, '
                f'nickname={(self.nickname if hasattr(self, "nickname") else None)!s}, '
                f'product_name={(self.product_name if hasattr(self, "product_name") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'line_of_business={(self.line_of_business if hasattr(self, "line_of_business") else None)!s}, '
                f'balance_type={(self.balance_type if hasattr(self, "balance_type") else None)!s}, '
                f'interest_rate={(self.interest_rate if hasattr(self, "interest_rate") else None)!s}, '
                f'interest_rate_type={(self.interest_rate_type if hasattr(self, "interest_rate_type") else None)!s}, '
                f'interest_rate_as_of={(self.interest_rate_as_of if hasattr(self, "interest_rate_as_of") else None)!s}, '
                f'last_activity_date={(self.last_activity_date if hasattr(self, "last_activity_date") else None)!s}, '
                f'micr_number={(self.micr_number if hasattr(self, "micr_number") else None)!s}, '
                f'parent_account_id={(self.parent_account_id if hasattr(self, "parent_account_id") else None)!s}, '
                f'prior_interest_rate={(self.prior_interest_rate if hasattr(self, "prior_interest_rate") else None)!s}, '
                f'transfer_in={(self.transfer_in if hasattr(self, "transfer_in") else None)!s}, '
                f'transfer_out={(self.transfer_out if hasattr(self, "transfer_out") else None)!s}, '
                f'compounding_period={(self.compounding_period if hasattr(self, "compounding_period") else None)!s}, '
                f'loan_term={(self.loan_term if hasattr(self, "loan_term") else None)!s}, '
                f'maturity_date={(self.maturity_date if hasattr(self, "maturity_date") else None)!s}, '
                f'originating_date={(self.originating_date if hasattr(self, "originating_date") else None)!s}, '
                f'payment_frequency={(self.payment_frequency if hasattr(self, "payment_frequency") else None)!s}, '
                f'total_number_of_payments={(self.total_number_of_payments if hasattr(self, "total_number_of_payments") else None)!s}, '
                f'balance_as_of={(self.balance_as_of if hasattr(self, "balance_as_of") else None)!s}, '
                f'escrow_balance={(self.escrow_balance if hasattr(self, "escrow_balance") else None)!s}, '
                f'interest_paid_year_to_date={(self.interest_paid_year_to_date if hasattr(self, "interest_paid_year_to_date") else None)!s}, '
                f'last_payment_amount={(self.last_payment_amount if hasattr(self, "last_payment_amount") else None)!s}, '
                f'last_payment_date={(self.last_payment_date if hasattr(self, "last_payment_date") else None)!s}, '
                f'next_payment_amount={(self.next_payment_amount if hasattr(self, "next_payment_amount") else None)!s}, '
                f'next_payment_date={(self.next_payment_date if hasattr(self, "next_payment_date") else None)!s}, '
                f'original_principal={(self.original_principal if hasattr(self, "original_principal") else None)!s}, '
                f'pay_off_amount={(self.pay_off_amount if hasattr(self, "pay_off_amount") else None)!s}, '
                f'principal_balance={(self.principal_balance if hasattr(self, "principal_balance") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
