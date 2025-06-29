# -*- coding: utf-8 -*-

"""
akoyaapisv240

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from akoyaapisv240.api_helper import APIHelper
from akoyaapisv240.models.individual_name import IndividualName


class HealthInsuranceCoveredIndividual(object):

    """Implementation of the 'Health Insurance Covered Individual' model.

    Used on Form 1095-B Part IV and Form 1095-C Part III

    Attributes:
        name (IndividualName): Name of responsible individual
        tin (str): Social security number or other TIN
        date_of_birth (date): Date of birth
        covered_all_12_months (bool): Covered all 12 months
        covered_months (List[MonthAbbreviationEnum]): Months covered

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "tin": 'tin',
        "date_of_birth": 'dateOfBirth',
        "covered_all_12_months": 'coveredAll12Months',
        "covered_months": 'coveredMonths'
    }

    _optionals = [
        'name',
        'tin',
        'date_of_birth',
        'covered_all_12_months',
        'covered_months',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 tin=APIHelper.SKIP,
                 date_of_birth=APIHelper.SKIP,
                 covered_all_12_months=APIHelper.SKIP,
                 covered_months=APIHelper.SKIP):
        """Constructor for the HealthInsuranceCoveredIndividual class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if tin is not APIHelper.SKIP:
            self.tin = tin 
        if date_of_birth is not APIHelper.SKIP:
            self.date_of_birth = date_of_birth 
        if covered_all_12_months is not APIHelper.SKIP:
            self.covered_all_12_months = covered_all_12_months 
        if covered_months is not APIHelper.SKIP:
            self.covered_months = covered_months 

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
        name = IndividualName.from_dictionary(dictionary.get('name')) if 'name' in dictionary.keys() else APIHelper.SKIP
        tin = dictionary.get("tin") if dictionary.get("tin") else APIHelper.SKIP
        date_of_birth = dateutil.parser.parse(dictionary.get('dateOfBirth')).date() if dictionary.get('dateOfBirth') else APIHelper.SKIP
        covered_all_12_months = dictionary.get("coveredAll12Months") if "coveredAll12Months" in dictionary.keys() else APIHelper.SKIP
        covered_months = dictionary.get("coveredMonths") if dictionary.get("coveredMonths") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   tin,
                   date_of_birth,
                   covered_all_12_months,
                   covered_months)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'tin={(self.tin if hasattr(self, "tin") else None)!r}, '
                f'date_of_birth={(self.date_of_birth if hasattr(self, "date_of_birth") else None)!r}, '
                f'covered_all_12_months={(self.covered_all_12_months if hasattr(self, "covered_all_12_months") else None)!r}, '
                f'covered_months={(self.covered_months if hasattr(self, "covered_months") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'tin={(self.tin if hasattr(self, "tin") else None)!s}, '
                f'date_of_birth={(self.date_of_birth if hasattr(self, "date_of_birth") else None)!s}, '
                f'covered_all_12_months={(self.covered_all_12_months if hasattr(self, "covered_all_12_months") else None)!s}, '
                f'covered_months={(self.covered_months if hasattr(self, "covered_months") else None)!s})')
