# -*- coding: utf-8 -*-

"""
akoya

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CompoundingPeriod(object):

    """Implementation of the 'CompoundingPeriod' enum.

    Attributes:
        DAILY: The enum member of type str.
        WEEKLY: The enum member of type str.
        BIWEEKLY: The enum member of type str.
        SEMIMONTHLY: The enum member of type str.
        MONTHLY: The enum member of type str.
        SEMIANNUALLY: The enum member of type str.
        ANNUALLY: The enum member of type str.
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """
    DAILY = 'DAILY'

    WEEKLY = 'WEEKLY'

    BIWEEKLY = 'BIWEEKLY'

    SEMIMONTHLY = 'SEMIMONTHLY'

    MONTHLY = 'MONTHLY'

    SEMIANNUALLY = 'SEMIANNUALLY'

    ANNUALLY = 'ANNUALLY'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return True if value else False 
