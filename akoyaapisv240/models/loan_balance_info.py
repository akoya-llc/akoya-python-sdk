# -*- coding: utf-8 -*-

"""
akoyaapisv240

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from akoyaapisv240.api_helper import APIHelper
from akoyaapisv240.models.loan_balances import LoanBalances


class LoanBalanceInfo(object):

    """Implementation of the 'LoanBalanceInfo' model.

    Attributes:
        loan_account (LoanBalances): Data elements included with balances
            specific to loan accounts

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "loan_account": 'loanAccount'
    }

    _optionals = [
        'loan_account',
    ]

    def __init__(self,
                 loan_account=APIHelper.SKIP):
        """Constructor for the LoanBalanceInfo class"""

        # Initialize members of the class
        if loan_account is not APIHelper.SKIP:
            self.loan_account = loan_account 

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
        loan_account = LoanBalances.from_dictionary(dictionary.get('loanAccount')) if 'loanAccount' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(loan_account)

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
                f'loan_account={(self.loan_account if hasattr(self, "loan_account") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'loan_account={(self.loan_account if hasattr(self, "loan_account") else None)!s})')
