# -*- coding: utf-8 -*-

"""
akoya

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class OrderType(object):

    """Implementation of the 'OrderType' enum.

    Type of order.

    Attributes:
        BUY: The enum member of type str.
        SELL: The enum member of type str.
        BUYTOCOVER: The enum member of type str.
        BUYTOOPEN: The enum member of type str.
        SELLTOCOVER: The enum member of type str.
        SELLTOOPEN: The enum member of type str.
        SELLSHORT: The enum member of type str.
        SELLCLOSE: The enum member of type str.
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """
    BUY = 'BUY'

    SELL = 'SELL'

    BUYTOCOVER = 'BUYTOCOVER'

    BUYTOOPEN = 'BUYTOOPEN'

    SELLTOCOVER = 'SELLTOCOVER'

    SELLTOOPEN = 'SELLTOOPEN'

    SELLSHORT = 'SELLSHORT'

    SELLCLOSE = 'SELLCLOSE'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return True if value else False 
