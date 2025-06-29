# -*- coding: utf-8 -*-

"""
akoyaapisv240

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class AnnunityValueBasisEnum(object):

    """Implementation of the 'AnnunityValueBasis' enum.

    Attributes:
        FIXED: The enum member of type str.
        VARIABLE: The enum member of type str.

    """
    _all_values = ['FIXED', 'VARIABLE']
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
        return value in cls._all_values
   