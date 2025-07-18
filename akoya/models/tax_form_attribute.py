# -*- coding: utf-8 -*-

"""
akoya

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from akoya.api_helper import APIHelper


class TaxFormAttribute(object):

    """Implementation of the 'Tax Form Attribute' model.

    An additional tax form attribute for use when a defined field is not
    available

    Attributes:
        name (str): Name of attribute
        value (str): Value of attribute
        box_number (str): Box number on a tax form, if any
        code (str): Tax form code for the given box number, if any
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "value": 'value',
        "box_number": 'boxNumber',
        "code": 'code'
    }

    _optionals = [
        'name',
        'value',
        'box_number',
        'code',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 value=APIHelper.SKIP,
                 box_number=APIHelper.SKIP,
                 code=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the TaxFormAttribute class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if value is not APIHelper.SKIP:
            self.value = value 
        if box_number is not APIHelper.SKIP:
            self.box_number = box_number 
        if code is not APIHelper.SKIP:
            self.code = code 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        value = dictionary.get("value") if dictionary.get("value") else APIHelper.SKIP
        box_number = dictionary.get("boxNumber") if dictionary.get("boxNumber") else APIHelper.SKIP
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items() if k not in cls._names.values()},
            unboxing_function=lambda value: value)
        # Return an object of this model
        return cls(name,
                   value,
                   box_number,
                   code,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'value={(self.value if hasattr(self, "value") else None)!r}, '
                f'box_number={(self.box_number if hasattr(self, "box_number") else None)!r}, '
                f'code={(self.code if hasattr(self, "code") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'value={(self.value if hasattr(self, "value") else None)!s}, '
                f'box_number={(self.box_number if hasattr(self, "box_number") else None)!s}, '
                f'code={(self.code if hasattr(self, "code") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
