# -*- coding: utf-8 -*-

"""
akoyaapisv240

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from akoyaapisv240.api_helper import APIHelper
from akoyaapisv240.configuration import Server
from akoyaapisv240.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from akoyaapisv240.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from akoyaapisv240.models.investments_details import InvestmentsDetails
from akoyaapisv240.models.taxlots_response import TaxlotsResponse
from akoyaapisv240.exceptions.error_error_exception import ErrorErrorException
from akoyaapisv240.exceptions.api_exception import APIException


class InvestmentsController(BaseController):

    """A Controller to access Endpoints in the akoyaapisv240 API."""
    def __init__(self, config):
        super(InvestmentsController, self).__init__(config)

    def get_accounts(self,
                     version,
                     provider_id,
                     x_akoya_interaction_type=None,
                     mode=None):
        """Does a GET request to /accounts/{version}/{providerId}.

        Get detailed account information that includes Akoya products Account
        Info and Balances for all account types (annunity, deposit, insurance,
        investments, line of credit, and loan) and adds the Investments
        product to investment accounts including contributions, holdings,
        vesting information, and more.
        To view the response schema, select the `200` response below. Then
        pick an option for annuity, deposit, insurance, investment, loan, and
        line of credit account types. 
        For an example payload response, see the `200` example response below
        the `Try it` feature. The example is from an investment account but
        all account types are supported and returned by this endpoint.
        > 🛑
        > 
        > The *id_token* should be used as the bearer token with this call.
        Use the `mode` query param to receive FDX-aligned, standardized data
        values (Beta). For example:
        `https://sandbox-products.ddp.akoya.com/accounts/v2/mikomo?mode=standar
        d`
        `mode` is available in both sandbox and production.
        `mode` is supported by a subset of providers. Log into the [Data
        Recipient Hub](https://recipient.ddp.akoya.com/login) and click
        [here](https://recipient.ddp.akoya.com/support/article/kA0Uw00000015GzK
        AI) to view a list of all providers supporting the `mode` parameter.

        Args:
            version (str): Akoya major version number. Do not use minor
                version numbers. For instance, use v2 and not v2.2
            provider_id (str): Id of provider
            x_akoya_interaction_type (InteractionTypeEnum, optional): Optional
                but recommended header to include with each data request. 
                Allowed values are `user` or `batch`.  `user` indicates a
                request is prompted by an end-user action. `batch` indicates
                the request is part of a batch process.
            mode (ModeEnum, optional): BETA. Default is raw. Use standard for
                FDX-aligned, standardized data values.

        Returns:
            InvestmentsDetails: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/accounts/{version}/{providerId}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('version')
                            .value(version)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('providerId')
                            .value(provider_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('x-akoya-interaction-type')
                          .value(x_akoya_interaction_type))
            .query_param(Parameter()
                         .key('mode')
                         .value(mode))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('acgAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(InvestmentsDetails.from_dictionary)
            .local_error('400', 'Invalid Input', ErrorErrorException)
            .local_error('401', 'Customer not authorized.', ErrorErrorException)
            .local_error('404', '701 - Tax Lots not found. The `holdingId` may be wrong.', ErrorErrorException)
            .local_error('405', 'Method Not Allowed', APIException)
            .local_error('406', 'Content Type not Supported', ErrorErrorException)
            .local_error('408', 'Request timed out (round trip call took >10 seconds).', ErrorErrorException)
            .local_error('429', '1207 - Too many requests', ErrorErrorException)
            .local_error('500', 'Catch-all exception where request was not processed due to an internal outage/issue.', ErrorErrorException)
            .local_error('501', 'FdxVersion in header is not implemented.', ErrorErrorException)
            .local_error('503', 'System is down for maintenance.', ErrorErrorException)
        ).execute()

    def get_taxlots(self,
                    version,
                    provider_id,
                    account_id,
                    holding_id,
                    x_akoya_interaction_type=None,
                    offset=None,
                    limit=None):
        """Does a GET request to /taxlots/{version}/{providerId}/{accountId}/{holdingId}.

        The taxlots API allows you to retrieve tax lots of
        consumer-permissioned accounts.
        > 🛑
        > 
        > The *id_token* should be used as the bearer token with this call.

        Args:
            version (str): Akoya major version number. Do not use minor
                version numbers. For instance, use v2 and not v2.2
            provider_id (str): Id of provider
            account_id (str): Account Identifier
            holding_id (str): Consumer's holdingId under investments
            x_akoya_interaction_type (InteractionTypeEnum, optional): Optional
                but recommended header to include with each data request. 
                Allowed values are `user` or `batch`.  `user` indicates a
                request is prompted by an end-user action. `batch` indicates
                the request is part of a batch process.
            offset (str, optional): The number of items to skip before the
                first in the response. The default is 0
            limit (str, optional): The maximum number of items to be returned
                in the response. The default is 50

        Returns:
            TaxlotsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/taxlots/{version}/{providerId}/{accountId}/{holdingId}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('version')
                            .value(version)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('providerId')
                            .value(provider_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('accountId')
                            .value(account_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('holdingId')
                            .value(holding_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('x-akoya-interaction-type')
                          .value(x_akoya_interaction_type))
            .query_param(Parameter()
                         .key('offset')
                         .value(offset))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('acgAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(TaxlotsResponse.from_dictionary)
            .local_error('401', 'Customer not authorized.', ErrorErrorException)
            .local_error('403', 'Incorrect providerId or no subscription to provider.', ErrorErrorException)
            .local_error('404', '701 - Tax Lots not found. The `holdingId` may be wrong.', ErrorErrorException)
            .local_error('405', 'Method Not Allowed', APIException)
            .local_error('408', 'Request timed out (round trip call took >10 seconds).', ErrorErrorException)
        ).execute()
