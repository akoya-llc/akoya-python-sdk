# -*- coding: utf-8 -*-

"""
akoyaapisv240

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from akoyaapisv240.api_helper import APIHelper


class TelephoneNumberPlusExtension(object):

    """Implementation of the 'Telephone Number Plus Extension' model.

    A telephone number that can contain optional text for an arbitrary length
    telephone extension number

    Attributes:
        mtype (TelephoneNumberTypeEnum): Type of phone number: HOME, BUSINESS,
            CELL, FAX
        country (ISO3166CountryCodeEnum): Country calling codes defined by
            ITU-T recommendations E.123 and E.164
        number (str): Telephone subscriber number defined by ITU-T
            recommendation E.164
        extension (str): An arbitrary length telephone number extension

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "country": 'country',
        "number": 'number',
        "extension": 'extension'
    }

    _optionals = [
        'mtype',
        'country',
        'number',
        'extension',
    ]

    def __init__(self,
                 mtype=APIHelper.SKIP,
                 country=APIHelper.SKIP,
                 number=APIHelper.SKIP,
                 extension=APIHelper.SKIP):
        """Constructor for the TelephoneNumberPlusExtension class"""

        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if country is not APIHelper.SKIP:
            self.country = country 
        if number is not APIHelper.SKIP:
            self.number = number 
        if extension is not APIHelper.SKIP:
            self.extension = extension 

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
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        country = dictionary.get("country") if dictionary.get("country") else APIHelper.SKIP
        number = dictionary.get("number") if dictionary.get("number") else APIHelper.SKIP
        extension = dictionary.get("extension") if dictionary.get("extension") else APIHelper.SKIP
        # Return an object of this model
        return cls(mtype,
                   country,
                   number,
                   extension)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!r}, '
                f'country={(self.country if hasattr(self, "country") else None)!r}, '
                f'number={(self.number if hasattr(self, "number") else None)!r}, '
                f'extension={(self.extension if hasattr(self, "extension") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'mtype={(self.mtype if hasattr(self, "mtype") else None)!s}, '
                f'country={(self.country if hasattr(self, "country") else None)!s}, '
                f'number={(self.number if hasattr(self, "number") else None)!s}, '
                f'extension={(self.extension if hasattr(self, "extension") else None)!s})')
