# -*- coding: utf-8 -*-

"""
akoya

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class AccountCategory(object):

    """Implementation of the 'AccountCategory' enum.

    The account category of the insurance account. Possible enums:
    DEPOSIT_ACCOUNT, INVESTMENT_ACCOUNT, LOAN_ACCOUNT, LOC_ACCOUNT,
    INSURANCE_ACCOUNT

    Attributes:
        DEPOSIT_ACCOUNT: The enum member of type str.
        INVESTMENT_ACCOUNT: The enum member of type str.
        LOAN_ACCOUNT: The enum member of type str.
        LOC_ACCOUNT: The enum member of type str.
        INSURANCE_ACCOUNT: The enum member of type str.
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """
    DEPOSIT_ACCOUNT = 'DEPOSIT_ACCOUNT'

    INVESTMENT_ACCOUNT = 'INVESTMENT_ACCOUNT'

    LOAN_ACCOUNT = 'LOAN_ACCOUNT'

    LOC_ACCOUNT = 'LOC_ACCOUNT'

    INSURANCE_ACCOUNT = 'INSURANCE_ACCOUNT'

    @classmethod
    def validate(cls, value):
        """Validates value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return True if value else False 
