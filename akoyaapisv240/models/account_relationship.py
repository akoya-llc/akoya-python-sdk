# -*- coding: utf-8 -*-

"""
akoyaapisv240

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from akoyaapisv240.api_helper import APIHelper


class AccountRelationship(object):

    """Implementation of the 'AccountRelationship' model.

    Attributes:
        account_id (str): Account ID of the related account
        relationship (RelationshipTypeEnum): Types of relationships between
            accounts and holders. Suggested values

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id": 'accountId',
        "relationship": 'relationship'
    }

    _optionals = [
        'account_id',
        'relationship',
    ]

    def __init__(self,
                 account_id=APIHelper.SKIP,
                 relationship=APIHelper.SKIP):
        """Constructor for the AccountRelationship class"""

        # Initialize members of the class
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if relationship is not APIHelper.SKIP:
            self.relationship = relationship 

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
        account_id = dictionary.get("accountId") if dictionary.get("accountId") else APIHelper.SKIP
        relationship = dictionary.get("relationship") if dictionary.get("relationship") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_id,
                   relationship)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!r}, '
                f'relationship={(self.relationship if hasattr(self, "relationship") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!s}, '
                f'relationship={(self.relationship if hasattr(self, "relationship") else None)!s})')
