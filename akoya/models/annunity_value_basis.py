# -*- coding: utf-8 -*-

"""
akoya

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class AnnunityValueBasis(object):

    """Implementation of the 'AnnunityValueBasis' enum.

    Attributes:
        FIXED: The enum member of type str.
        VARIABLE: The enum member of type str.
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """
    FIXED = 'FIXED'

    VARIABLE = 'VARIABLE'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return True if value else False 
