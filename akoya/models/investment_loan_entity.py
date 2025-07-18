# -*- coding: utf-8 -*-

"""
akoya

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from akoya.api_helper import APIHelper


class InvestmentLoanEntity(object):

    """Implementation of the 'InvestmentLoan Entity' model.

    Information about an investment loan.

    Attributes:
        loan_id (str): Unique identifier for this loan
        loan_description (str): Description
        initial_loan_balance (float): Initial loan balance amount
        loan_start_date (datetime): Start date of the loan
        current_loan_balance (float): Current loan principal balance amount
        date_as_of (datetime): Date and time of current loan balance
        loan_rate (float): Loan annual interest rate for the loan
        loan_payment_amount (float): Loan payment amount
        loan_payment_frequency (LoanPaymentFrequency): The model property of
            type LoanPaymentFrequency.
        loan_payment_initial (float): Initial number of loan payments
        loan_payments_remaining (int): Remaining number of loan payments
        loan_maturity_date (datetime): Expected loan end date
        loan_interest_to_date (float): Total interest paid to date on this loan
        loan_total_projected_interest (float): Total projected interest to be
            paid on this loan
        loan_next_payment_date (datetime): The next payment date for the loan
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "loan_id": 'loanId',
        "loan_description": 'loanDescription',
        "initial_loan_balance": 'initialLoanBalance',
        "loan_start_date": 'loanStartDate',
        "current_loan_balance": 'currentLoanBalance',
        "date_as_of": 'dateAsOf',
        "loan_rate": 'loanRate',
        "loan_payment_amount": 'loanPaymentAmount',
        "loan_payment_frequency": 'loanPaymentFrequency',
        "loan_payment_initial": 'loanPaymentInitial',
        "loan_payments_remaining": 'loanPaymentsRemaining',
        "loan_maturity_date": 'loanMaturityDate',
        "loan_interest_to_date": 'loanInterestToDate',
        "loan_total_projected_interest": 'loanTotalProjectedInterest',
        "loan_next_payment_date": 'loanNextPaymentDate'
    }

    _optionals = [
        'loan_id',
        'loan_description',
        'initial_loan_balance',
        'loan_start_date',
        'current_loan_balance',
        'date_as_of',
        'loan_rate',
        'loan_payment_amount',
        'loan_payment_frequency',
        'loan_payment_initial',
        'loan_payments_remaining',
        'loan_maturity_date',
        'loan_interest_to_date',
        'loan_total_projected_interest',
        'loan_next_payment_date',
    ]

    def __init__(self,
                 loan_id=APIHelper.SKIP,
                 loan_description=APIHelper.SKIP,
                 initial_loan_balance=APIHelper.SKIP,
                 loan_start_date=APIHelper.SKIP,
                 current_loan_balance=APIHelper.SKIP,
                 date_as_of=APIHelper.SKIP,
                 loan_rate=APIHelper.SKIP,
                 loan_payment_amount=APIHelper.SKIP,
                 loan_payment_frequency=APIHelper.SKIP,
                 loan_payment_initial=APIHelper.SKIP,
                 loan_payments_remaining=APIHelper.SKIP,
                 loan_maturity_date=APIHelper.SKIP,
                 loan_interest_to_date=APIHelper.SKIP,
                 loan_total_projected_interest=APIHelper.SKIP,
                 loan_next_payment_date=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvestmentLoanEntity class"""

        # Initialize members of the class
        if loan_id is not APIHelper.SKIP:
            self.loan_id = loan_id 
        if loan_description is not APIHelper.SKIP:
            self.loan_description = loan_description 
        if initial_loan_balance is not APIHelper.SKIP:
            self.initial_loan_balance = initial_loan_balance 
        if loan_start_date is not APIHelper.SKIP:
            self.loan_start_date = APIHelper.apply_datetime_converter(loan_start_date, APIHelper.RFC3339DateTime) if loan_start_date else None 
        if current_loan_balance is not APIHelper.SKIP:
            self.current_loan_balance = current_loan_balance 
        if date_as_of is not APIHelper.SKIP:
            self.date_as_of = APIHelper.apply_datetime_converter(date_as_of, APIHelper.RFC3339DateTime) if date_as_of else None 
        if loan_rate is not APIHelper.SKIP:
            self.loan_rate = loan_rate 
        if loan_payment_amount is not APIHelper.SKIP:
            self.loan_payment_amount = loan_payment_amount 
        if loan_payment_frequency is not APIHelper.SKIP:
            self.loan_payment_frequency = loan_payment_frequency 
        if loan_payment_initial is not APIHelper.SKIP:
            self.loan_payment_initial = loan_payment_initial 
        if loan_payments_remaining is not APIHelper.SKIP:
            self.loan_payments_remaining = loan_payments_remaining 
        if loan_maturity_date is not APIHelper.SKIP:
            self.loan_maturity_date = APIHelper.apply_datetime_converter(loan_maturity_date, APIHelper.RFC3339DateTime) if loan_maturity_date else None 
        if loan_interest_to_date is not APIHelper.SKIP:
            self.loan_interest_to_date = loan_interest_to_date 
        if loan_total_projected_interest is not APIHelper.SKIP:
            self.loan_total_projected_interest = loan_total_projected_interest 
        if loan_next_payment_date is not APIHelper.SKIP:
            self.loan_next_payment_date = APIHelper.apply_datetime_converter(loan_next_payment_date, APIHelper.RFC3339DateTime) if loan_next_payment_date else None 

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
        loan_id = dictionary.get("loanId") if dictionary.get("loanId") else APIHelper.SKIP
        loan_description = dictionary.get("loanDescription") if dictionary.get("loanDescription") else APIHelper.SKIP
        initial_loan_balance = dictionary.get("initialLoanBalance") if dictionary.get("initialLoanBalance") else APIHelper.SKIP
        loan_start_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("loanStartDate")).datetime if dictionary.get("loanStartDate") else APIHelper.SKIP
        current_loan_balance = dictionary.get("currentLoanBalance") if dictionary.get("currentLoanBalance") else APIHelper.SKIP
        date_as_of = APIHelper.RFC3339DateTime.from_value(dictionary.get("dateAsOf")).datetime if dictionary.get("dateAsOf") else APIHelper.SKIP
        loan_rate = dictionary.get("loanRate") if dictionary.get("loanRate") else APIHelper.SKIP
        loan_payment_amount = dictionary.get("loanPaymentAmount") if dictionary.get("loanPaymentAmount") else APIHelper.SKIP
        loan_payment_frequency = dictionary.get("loanPaymentFrequency") if dictionary.get("loanPaymentFrequency") else APIHelper.SKIP
        loan_payment_initial = dictionary.get("loanPaymentInitial") if dictionary.get("loanPaymentInitial") else APIHelper.SKIP
        loan_payments_remaining = dictionary.get("loanPaymentsRemaining") if dictionary.get("loanPaymentsRemaining") else APIHelper.SKIP
        loan_maturity_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("loanMaturityDate")).datetime if dictionary.get("loanMaturityDate") else APIHelper.SKIP
        loan_interest_to_date = dictionary.get("loanInterestToDate") if dictionary.get("loanInterestToDate") else APIHelper.SKIP
        loan_total_projected_interest = dictionary.get("loanTotalProjectedInterest") if dictionary.get("loanTotalProjectedInterest") else APIHelper.SKIP
        loan_next_payment_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("loanNextPaymentDate")).datetime if dictionary.get("loanNextPaymentDate") else APIHelper.SKIP
        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items() if k not in cls._names.values()},
            unboxing_function=lambda value: value)
        # Return an object of this model
        return cls(loan_id,
                   loan_description,
                   initial_loan_balance,
                   loan_start_date,
                   current_loan_balance,
                   date_as_of,
                   loan_rate,
                   loan_payment_amount,
                   loan_payment_frequency,
                   loan_payment_initial,
                   loan_payments_remaining,
                   loan_maturity_date,
                   loan_interest_to_date,
                   loan_total_projected_interest,
                   loan_next_payment_date,
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
                f'loan_id={(self.loan_id if hasattr(self, "loan_id") else None)!r}, '
                f'loan_description={(self.loan_description if hasattr(self, "loan_description") else None)!r}, '
                f'initial_loan_balance={(self.initial_loan_balance if hasattr(self, "initial_loan_balance") else None)!r}, '
                f'loan_start_date={(self.loan_start_date if hasattr(self, "loan_start_date") else None)!r}, '
                f'current_loan_balance={(self.current_loan_balance if hasattr(self, "current_loan_balance") else None)!r}, '
                f'date_as_of={(self.date_as_of if hasattr(self, "date_as_of") else None)!r}, '
                f'loan_rate={(self.loan_rate if hasattr(self, "loan_rate") else None)!r}, '
                f'loan_payment_amount={(self.loan_payment_amount if hasattr(self, "loan_payment_amount") else None)!r}, '
                f'loan_payment_frequency={(self.loan_payment_frequency if hasattr(self, "loan_payment_frequency") else None)!r}, '
                f'loan_payment_initial={(self.loan_payment_initial if hasattr(self, "loan_payment_initial") else None)!r}, '
                f'loan_payments_remaining={(self.loan_payments_remaining if hasattr(self, "loan_payments_remaining") else None)!r}, '
                f'loan_maturity_date={(self.loan_maturity_date if hasattr(self, "loan_maturity_date") else None)!r}, '
                f'loan_interest_to_date={(self.loan_interest_to_date if hasattr(self, "loan_interest_to_date") else None)!r}, '
                f'loan_total_projected_interest={(self.loan_total_projected_interest if hasattr(self, "loan_total_projected_interest") else None)!r}, '
                f'loan_next_payment_date={(self.loan_next_payment_date if hasattr(self, "loan_next_payment_date") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'loan_id={(self.loan_id if hasattr(self, "loan_id") else None)!s}, '
                f'loan_description={(self.loan_description if hasattr(self, "loan_description") else None)!s}, '
                f'initial_loan_balance={(self.initial_loan_balance if hasattr(self, "initial_loan_balance") else None)!s}, '
                f'loan_start_date={(self.loan_start_date if hasattr(self, "loan_start_date") else None)!s}, '
                f'current_loan_balance={(self.current_loan_balance if hasattr(self, "current_loan_balance") else None)!s}, '
                f'date_as_of={(self.date_as_of if hasattr(self, "date_as_of") else None)!s}, '
                f'loan_rate={(self.loan_rate if hasattr(self, "loan_rate") else None)!s}, '
                f'loan_payment_amount={(self.loan_payment_amount if hasattr(self, "loan_payment_amount") else None)!s}, '
                f'loan_payment_frequency={(self.loan_payment_frequency if hasattr(self, "loan_payment_frequency") else None)!s}, '
                f'loan_payment_initial={(self.loan_payment_initial if hasattr(self, "loan_payment_initial") else None)!s}, '
                f'loan_payments_remaining={(self.loan_payments_remaining if hasattr(self, "loan_payments_remaining") else None)!s}, '
                f'loan_maturity_date={(self.loan_maturity_date if hasattr(self, "loan_maturity_date") else None)!s}, '
                f'loan_interest_to_date={(self.loan_interest_to_date if hasattr(self, "loan_interest_to_date") else None)!s}, '
                f'loan_total_projected_interest={(self.loan_total_projected_interest if hasattr(self, "loan_total_projected_interest") else None)!s}, '
                f'loan_next_payment_date={(self.loan_next_payment_date if hasattr(self, "loan_next_payment_date") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
