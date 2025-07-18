# -*- coding: utf-8 -*-

"""
akoya

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from akoya.api_helper import APIHelper
from akoya.models.deposit_balances import DepositBalances


class DepositBalance(object):

    """Implementation of the 'DepositBalance' model.

    Attributes:
        deposit_account (DepositBalances): Data elements included with
            balances specific to deposit accounts
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "deposit_account": 'depositAccount'
    }

    _optionals = [
        'deposit_account',
    ]

    def __init__(self,
                 deposit_account=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the DepositBalance class"""

        # Initialize members of the class
        if deposit_account is not APIHelper.SKIP:
            self.deposit_account = deposit_account 

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
        deposit_account = DepositBalances.from_dictionary(dictionary.get('depositAccount')) if 'depositAccount' in dictionary.keys() else APIHelper.SKIP
        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items() if k not in cls._names.values()},
            unboxing_function=lambda value: value)
        # Return an object of this model
        return cls(deposit_account,
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
                f'deposit_account={(self.deposit_account if hasattr(self, "deposit_account") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'deposit_account={(self.deposit_account if hasattr(self, "deposit_account") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
