# -*- coding: utf-8 -*-

"""
akoyaapisv240

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ResultTypeEnum(object):

    """Implementation of the 'Result Type' enum.

    Flag to indicate if you want a lightweight array of metadata
    (AccountDescriptor or Tax or Operations) or full item details (Account or
    a Tax subclass or Availability details). If set to 'lightweight', should
    only return the fields associated with the metadata entity.

    Attributes:
        DETAILS: The enum member of type str.
        LIGHTWEIGHT: The enum member of type str.

    """
    DETAILS = 'details'

    LIGHTWEIGHT = 'lightweight'

