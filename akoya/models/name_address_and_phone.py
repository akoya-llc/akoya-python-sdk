# -*- coding: utf-8 -*-

"""
akoya

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from akoya.api_helper import APIHelper
from akoya.models.telephone_number_plus_extension import TelephoneNumberPlusExtension


class NameAddressAndPhone(object):

    """Implementation of the 'Name, Address and Phone' model.

    Contact phone number with name and address

    Attributes:
        line_1 (str): Address line 1
        line_2 (str): Address line 2
        line_3 (str): Address line 3
        city (str): City
        region (str): State, Province, Territory, Canton or Prefecture. From
            [Universal Postal
            Union](https://www.upu.int/en/Postal-Solutions/Programmes-Services/
            Addressing-Solutions#addressing-s42-standard) as of 2-26-2020,
            [S42 International Address
            Standards](https://www.upu.int/UPU/media/upu/documents/PostCode/S42
            _International-Addressing-Standards.pdf). For U.S. addresses can
            be 2-character code from '#/components/schemas/StateCode'
        postal_code (str): Postal code
        country (Iso3166CountryCode): Country code
        name_1 (str): Name line 1
        name_2 (str): Name line 2
        phone (TelephoneNumberPlusExtension): A telephone number that can
            contain optional text for an arbitrary length telephone extension
            number
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "line_1": 'line1',
        "line_2": 'line2',
        "line_3": 'line3',
        "city": 'city',
        "region": 'region',
        "postal_code": 'postalCode',
        "country": 'country',
        "name_1": 'name1',
        "name_2": 'name2',
        "phone": 'phone'
    }

    _optionals = [
        'line_1',
        'line_2',
        'line_3',
        'city',
        'region',
        'postal_code',
        'country',
        'name_1',
        'name_2',
        'phone',
    ]

    def __init__(self,
                 line_1=APIHelper.SKIP,
                 line_2=APIHelper.SKIP,
                 line_3=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 region=APIHelper.SKIP,
                 postal_code=APIHelper.SKIP,
                 country=APIHelper.SKIP,
                 name_1=APIHelper.SKIP,
                 name_2=APIHelper.SKIP,
                 phone=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the NameAddressAndPhone class"""

        # Initialize members of the class
        if line_1 is not APIHelper.SKIP:
            self.line_1 = line_1 
        if line_2 is not APIHelper.SKIP:
            self.line_2 = line_2 
        if line_3 is not APIHelper.SKIP:
            self.line_3 = line_3 
        if city is not APIHelper.SKIP:
            self.city = city 
        if region is not APIHelper.SKIP:
            self.region = region 
        if postal_code is not APIHelper.SKIP:
            self.postal_code = postal_code 
        if country is not APIHelper.SKIP:
            self.country = country 
        if name_1 is not APIHelper.SKIP:
            self.name_1 = name_1 
        if name_2 is not APIHelper.SKIP:
            self.name_2 = name_2 
        if phone is not APIHelper.SKIP:
            self.phone = phone 

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
        line_1 = dictionary.get("line1") if dictionary.get("line1") else APIHelper.SKIP
        line_2 = dictionary.get("line2") if dictionary.get("line2") else APIHelper.SKIP
        line_3 = dictionary.get("line3") if dictionary.get("line3") else APIHelper.SKIP
        city = dictionary.get("city") if dictionary.get("city") else APIHelper.SKIP
        region = dictionary.get("region") if dictionary.get("region") else APIHelper.SKIP
        postal_code = dictionary.get("postalCode") if dictionary.get("postalCode") else APIHelper.SKIP
        country = dictionary.get("country") if dictionary.get("country") else APIHelper.SKIP
        name_1 = dictionary.get("name1") if dictionary.get("name1") else APIHelper.SKIP
        name_2 = dictionary.get("name2") if dictionary.get("name2") else APIHelper.SKIP
        phone = TelephoneNumberPlusExtension.from_dictionary(dictionary.get('phone')) if 'phone' in dictionary.keys() else APIHelper.SKIP
        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items() if k not in cls._names.values()},
            unboxing_function=lambda value: value)
        # Return an object of this model
        return cls(line_1,
                   line_2,
                   line_3,
                   city,
                   region,
                   postal_code,
                   country,
                   name_1,
                   name_2,
                   phone,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'line_1={(self.line_1 if hasattr(self, "line_1") else None)!r}, '
                f'line_2={(self.line_2 if hasattr(self, "line_2") else None)!r}, '
                f'line_3={(self.line_3 if hasattr(self, "line_3") else None)!r}, '
                f'city={(self.city if hasattr(self, "city") else None)!r}, '
                f'region={(self.region if hasattr(self, "region") else None)!r}, '
                f'postal_code={(self.postal_code if hasattr(self, "postal_code") else None)!r}, '
                f'country={(self.country if hasattr(self, "country") else None)!r}, '
                f'name_1={(self.name_1 if hasattr(self, "name_1") else None)!r}, '
                f'name_2={(self.name_2 if hasattr(self, "name_2") else None)!r}, '
                f'phone={(self.phone if hasattr(self, "phone") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'line_1={(self.line_1 if hasattr(self, "line_1") else None)!s}, '
                f'line_2={(self.line_2 if hasattr(self, "line_2") else None)!s}, '
                f'line_3={(self.line_3 if hasattr(self, "line_3") else None)!s}, '
                f'city={(self.city if hasattr(self, "city") else None)!s}, '
                f'region={(self.region if hasattr(self, "region") else None)!s}, '
                f'postal_code={(self.postal_code if hasattr(self, "postal_code") else None)!s}, '
                f'country={(self.country if hasattr(self, "country") else None)!s}, '
                f'name_1={(self.name_1 if hasattr(self, "name_1") else None)!s}, '
                f'name_2={(self.name_2 if hasattr(self, "name_2") else None)!s}, '
                f'phone={(self.phone if hasattr(self, "phone") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
