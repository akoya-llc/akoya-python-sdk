# -*- coding: utf-8 -*-

"""
akoya

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from akoya.api_helper import APIHelper


class OauthToken(object):

    """Implementation of the 'OAuthToken' model.

    OAuth 2 Authorization endpoint response

    Attributes:
        id_token (str): ID Token
        token_type (str): Type of access token
        expires_in (int): Time in seconds before the access token expires
        scope (str): List of scopes granted This is a space-delimited list of
            strings.
        expiry (int): Time of token expiry as unix timestamp (UTC)
        refresh_token (str): Refresh token Used to get a new access token when
            it expires.
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id_token": 'id_token',
        "token_type": 'token_type',
        "expires_in": 'expires_in',
        "scope": 'scope',
        "expiry": 'expiry',
        "refresh_token": 'refresh_token'
    }

    _optionals = [
        'expires_in',
        'scope',
        'expiry',
        'refresh_token',
    ]

    def __init__(self,
                 id_token=None,
                 token_type=None,
                 expires_in=APIHelper.SKIP,
                 scope=APIHelper.SKIP,
                 expiry=APIHelper.SKIP,
                 refresh_token=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the OauthToken class"""

        # Initialize members of the class
        self.id_token = id_token 
        self.token_type = token_type 
        if expires_in is not APIHelper.SKIP:
            self.expires_in = expires_in 
        if scope is not APIHelper.SKIP:
            self.scope = scope 
        if expiry is not APIHelper.SKIP:
            self.expiry = expiry 
        if refresh_token is not APIHelper.SKIP:
            self.refresh_token = refresh_token 

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
        id_token = dictionary.get("id_token") if dictionary.get("id_token") else None
        token_type = dictionary.get("token_type") if dictionary.get("token_type") else None
        expires_in = dictionary.get("expires_in") if dictionary.get("expires_in") else APIHelper.SKIP
        scope = dictionary.get("scope") if dictionary.get("scope") else APIHelper.SKIP
        expiry = dictionary.get("expiry") if dictionary.get("expiry") else APIHelper.SKIP
        refresh_token = dictionary.get("refresh_token") if dictionary.get("refresh_token") else APIHelper.SKIP
        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items() if k not in cls._names.values()},
            unboxing_function=lambda value: value)
        # Return an object of this model
        return cls(id_token,
                   token_type,
                   expires_in,
                   scope,
                   expiry,
                   refresh_token,
                   additional_properties)
