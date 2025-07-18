# -*- coding: utf-8 -*-

"""
akoya

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from akoya.api_helper import APIHelper


class PaymentDetails(object):

    """Implementation of the 'PaymentDetails' model.

    Payment details for some transactions

    Attributes:
        escrow_amount (float): The amount of payment applied to escrow
        fees_amount (float): The amount of payment applied to fees
        insurance_amount (float): The amount of payment applied to
            life/health/accident insurance on the loan
        interest_amount (float): The amount of payment applied to interest
        pmi_amount (float): The amount of payment applied to PMI
        principal_amount (float): The amount of payment applied to principal
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "escrow_amount": 'escrowAmount',
        "fees_amount": 'feesAmount',
        "insurance_amount": 'insuranceAmount',
        "interest_amount": 'interestAmount',
        "pmi_amount": 'pmiAmount',
        "principal_amount": 'principalAmount'
    }

    _optionals = [
        'escrow_amount',
        'fees_amount',
        'insurance_amount',
        'interest_amount',
        'pmi_amount',
        'principal_amount',
    ]

    def __init__(self,
                 escrow_amount=APIHelper.SKIP,
                 fees_amount=APIHelper.SKIP,
                 insurance_amount=APIHelper.SKIP,
                 interest_amount=APIHelper.SKIP,
                 pmi_amount=APIHelper.SKIP,
                 principal_amount=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the PaymentDetails class"""

        # Initialize members of the class
        if escrow_amount is not APIHelper.SKIP:
            self.escrow_amount = escrow_amount 
        if fees_amount is not APIHelper.SKIP:
            self.fees_amount = fees_amount 
        if insurance_amount is not APIHelper.SKIP:
            self.insurance_amount = insurance_amount 
        if interest_amount is not APIHelper.SKIP:
            self.interest_amount = interest_amount 
        if pmi_amount is not APIHelper.SKIP:
            self.pmi_amount = pmi_amount 
        if principal_amount is not APIHelper.SKIP:
            self.principal_amount = principal_amount 

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
        escrow_amount = dictionary.get("escrowAmount") if dictionary.get("escrowAmount") else APIHelper.SKIP
        fees_amount = dictionary.get("feesAmount") if dictionary.get("feesAmount") else APIHelper.SKIP
        insurance_amount = dictionary.get("insuranceAmount") if dictionary.get("insuranceAmount") else APIHelper.SKIP
        interest_amount = dictionary.get("interestAmount") if dictionary.get("interestAmount") else APIHelper.SKIP
        pmi_amount = dictionary.get("pmiAmount") if dictionary.get("pmiAmount") else APIHelper.SKIP
        principal_amount = dictionary.get("principalAmount") if dictionary.get("principalAmount") else APIHelper.SKIP
        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items() if k not in cls._names.values()},
            unboxing_function=lambda value: value)
        # Return an object of this model
        return cls(escrow_amount,
                   fees_amount,
                   insurance_amount,
                   interest_amount,
                   pmi_amount,
                   principal_amount,
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
                f'escrow_amount={(self.escrow_amount if hasattr(self, "escrow_amount") else None)!r}, '
                f'fees_amount={(self.fees_amount if hasattr(self, "fees_amount") else None)!r}, '
                f'insurance_amount={(self.insurance_amount if hasattr(self, "insurance_amount") else None)!r}, '
                f'interest_amount={(self.interest_amount if hasattr(self, "interest_amount") else None)!r}, '
                f'pmi_amount={(self.pmi_amount if hasattr(self, "pmi_amount") else None)!r}, '
                f'principal_amount={(self.principal_amount if hasattr(self, "principal_amount") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'escrow_amount={(self.escrow_amount if hasattr(self, "escrow_amount") else None)!s}, '
                f'fees_amount={(self.fees_amount if hasattr(self, "fees_amount") else None)!s}, '
                f'insurance_amount={(self.insurance_amount if hasattr(self, "insurance_amount") else None)!s}, '
                f'interest_amount={(self.interest_amount if hasattr(self, "interest_amount") else None)!s}, '
                f'pmi_amount={(self.pmi_amount if hasattr(self, "pmi_amount") else None)!s}, '
                f'principal_amount={(self.principal_amount if hasattr(self, "principal_amount") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
