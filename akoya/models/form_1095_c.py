# -*- coding: utf-8 -*-

"""
akoya

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from akoya.api_helper import APIHelper
from akoya.models.error import Error
from akoya.models.hateoas_link import HateoasLink
from akoya.models.health_insurance_marketplace_covered_individual import HealthInsuranceMarketplaceCoveredIndividual
from akoya.models.offer_of_health_insurance_coverage import OfferOfHealthInsuranceCoverage
from akoya.models.tax_form_attribute import TaxFormAttribute
from akoya.models.tax_party import TaxParty


class Form1095C(object):

    """Implementation of the 'Form 1095-C' model.

    Employer-Provided Health Insurance Offer and Coverage

    Attributes:
        tax_year (int): Year for which taxes are being paid
        corrected (bool): True to indicate this is a corrected tax form
        account_id (str): Long-term persistent identity of the source account.
            Not the account number
        tax_form_id (str): Long-term persistent id for this tax form.
            Depending upon the data provider, this may be the same id as the
            enclosing tax statement id, or this may be a different id, or this
            id may be omitted.
        tax_form_date (date): Date of production or delivery of the tax form
        additional_information (str): Additional explanation text or content
            about this tax form
        tax_form_type (TypeFormType): Enumerated name of the tax form entity
            e.g. "TaxW2"
        issuer (TaxParty): Issuer's name, address, phone, and TIN. Issuer data
            need only be transmitted on enclosing TaxStatement, if it is the
            same on all its included tax forms.
        recipient (TaxParty): Recipient's name, address, phone, and TIN.
            Recipient data need only be transmitted on enclosing TaxStatement,
            if it is the same on all its included tax forms.
        attributes (List[TaxFormAttribute]): Additional attributes for this
            tax form when defined fields are not available. Some specific
            additional attributes already defined by providers: Fields
            required by [IRS
            FIRE](https://www.irs.gov/e-file-providers/filing-information-retur
            ns-electronically-fire): Name Control, Type of Identification
            Number (EIN, SSN, ITIN, ATIN). (ATIN is tax ID number for pending
            adoptions.) Tax form provider field for taxpayer notification:
            Recipient Email Address.
        error (Error): Present if an error was encountered while retrieving
            this form
        links (List[HateoasLink]): Links to retrieve this form as data or
            image, or to invoke other APIs
        self_insured_coverage (bool): Self Insured Coverage
        offers_of_coverage (List[OfferOfHealthInsuranceCoverage]): Boxes
            14-16, Employee Offer of Coverage
        employee_age (int): Employee's Age on January 1
        plan_start_month (int): Plan Start Month
        covered_individuals
            (List[HealthInsuranceMarketplaceCoveredIndividual]): Boxes 17+,
            Covered Individuals
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tax_year": 'taxYear',
        "corrected": 'corrected',
        "account_id": 'accountId',
        "tax_form_id": 'taxFormId',
        "tax_form_date": 'taxFormDate',
        "additional_information": 'additionalInformation',
        "tax_form_type": 'taxFormType',
        "issuer": 'issuer',
        "recipient": 'recipient',
        "attributes": 'attributes',
        "error": 'error',
        "links": 'links',
        "self_insured_coverage": 'selfInsuredCoverage',
        "offers_of_coverage": 'offersOfCoverage',
        "employee_age": 'employeeAge',
        "plan_start_month": 'planStartMonth',
        "covered_individuals": 'coveredIndividuals'
    }

    _optionals = [
        'tax_year',
        'corrected',
        'account_id',
        'tax_form_id',
        'tax_form_date',
        'additional_information',
        'tax_form_type',
        'issuer',
        'recipient',
        'attributes',
        'error',
        'links',
        'self_insured_coverage',
        'offers_of_coverage',
        'employee_age',
        'plan_start_month',
        'covered_individuals',
    ]

    def __init__(self,
                 tax_year=APIHelper.SKIP,
                 corrected=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 tax_form_id=APIHelper.SKIP,
                 tax_form_date=APIHelper.SKIP,
                 additional_information=APIHelper.SKIP,
                 tax_form_type=APIHelper.SKIP,
                 issuer=APIHelper.SKIP,
                 recipient=APIHelper.SKIP,
                 attributes=APIHelper.SKIP,
                 error=APIHelper.SKIP,
                 links=APIHelper.SKIP,
                 self_insured_coverage=APIHelper.SKIP,
                 offers_of_coverage=APIHelper.SKIP,
                 employee_age=APIHelper.SKIP,
                 plan_start_month=APIHelper.SKIP,
                 covered_individuals=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Form1095C class"""

        # Initialize members of the class
        if tax_year is not APIHelper.SKIP:
            self.tax_year = tax_year 
        if corrected is not APIHelper.SKIP:
            self.corrected = corrected 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if tax_form_id is not APIHelper.SKIP:
            self.tax_form_id = tax_form_id 
        if tax_form_date is not APIHelper.SKIP:
            self.tax_form_date = tax_form_date 
        if additional_information is not APIHelper.SKIP:
            self.additional_information = additional_information 
        if tax_form_type is not APIHelper.SKIP:
            self.tax_form_type = tax_form_type 
        if issuer is not APIHelper.SKIP:
            self.issuer = issuer 
        if recipient is not APIHelper.SKIP:
            self.recipient = recipient 
        if attributes is not APIHelper.SKIP:
            self.attributes = attributes 
        if error is not APIHelper.SKIP:
            self.error = error 
        if links is not APIHelper.SKIP:
            self.links = links 
        if self_insured_coverage is not APIHelper.SKIP:
            self.self_insured_coverage = self_insured_coverage 
        if offers_of_coverage is not APIHelper.SKIP:
            self.offers_of_coverage = offers_of_coverage 
        if employee_age is not APIHelper.SKIP:
            self.employee_age = employee_age 
        if plan_start_month is not APIHelper.SKIP:
            self.plan_start_month = plan_start_month 
        if covered_individuals is not APIHelper.SKIP:
            self.covered_individuals = covered_individuals 

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
        tax_year = dictionary.get("taxYear") if dictionary.get("taxYear") else APIHelper.SKIP
        corrected = dictionary.get("corrected") if "corrected" in dictionary.keys() else APIHelper.SKIP
        account_id = dictionary.get("accountId") if dictionary.get("accountId") else APIHelper.SKIP
        tax_form_id = dictionary.get("taxFormId") if dictionary.get("taxFormId") else APIHelper.SKIP
        tax_form_date = dateutil.parser.parse(dictionary.get('taxFormDate')).date() if dictionary.get('taxFormDate') else APIHelper.SKIP
        additional_information = dictionary.get("additionalInformation") if dictionary.get("additionalInformation") else APIHelper.SKIP
        tax_form_type = dictionary.get("taxFormType") if dictionary.get("taxFormType") else APIHelper.SKIP
        issuer = TaxParty.from_dictionary(dictionary.get('issuer')) if 'issuer' in dictionary.keys() else APIHelper.SKIP
        recipient = TaxParty.from_dictionary(dictionary.get('recipient')) if 'recipient' in dictionary.keys() else APIHelper.SKIP
        attributes = None
        if dictionary.get('attributes') is not None:
            attributes = [TaxFormAttribute.from_dictionary(x) for x in dictionary.get('attributes')]
        else:
            attributes = APIHelper.SKIP
        error = Error.from_dictionary(dictionary.get('error')) if 'error' in dictionary.keys() else APIHelper.SKIP
        links = None
        if dictionary.get('links') is not None:
            links = [HateoasLink.from_dictionary(x) for x in dictionary.get('links')]
        else:
            links = APIHelper.SKIP
        self_insured_coverage = dictionary.get("selfInsuredCoverage") if "selfInsuredCoverage" in dictionary.keys() else APIHelper.SKIP
        offers_of_coverage = None
        if dictionary.get('offersOfCoverage') is not None:
            offers_of_coverage = [OfferOfHealthInsuranceCoverage.from_dictionary(x) for x in dictionary.get('offersOfCoverage')]
        else:
            offers_of_coverage = APIHelper.SKIP
        employee_age = dictionary.get("employeeAge") if dictionary.get("employeeAge") else APIHelper.SKIP
        plan_start_month = dictionary.get("planStartMonth") if dictionary.get("planStartMonth") else APIHelper.SKIP
        covered_individuals = None
        if dictionary.get('coveredIndividuals') is not None:
            covered_individuals = [HealthInsuranceMarketplaceCoveredIndividual.from_dictionary(x) for x in dictionary.get('coveredIndividuals')]
        else:
            covered_individuals = APIHelper.SKIP
        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items() if k not in cls._names.values()},
            unboxing_function=lambda value: value)
        # Return an object of this model
        return cls(tax_year,
                   corrected,
                   account_id,
                   tax_form_id,
                   tax_form_date,
                   additional_information,
                   tax_form_type,
                   issuer,
                   recipient,
                   attributes,
                   error,
                   links,
                   self_insured_coverage,
                   offers_of_coverage,
                   employee_age,
                   plan_start_month,
                   covered_individuals,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'tax_year={(self.tax_year if hasattr(self, "tax_year") else None)!r}, '
                f'corrected={(self.corrected if hasattr(self, "corrected") else None)!r}, '
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!r}, '
                f'tax_form_id={(self.tax_form_id if hasattr(self, "tax_form_id") else None)!r}, '
                f'tax_form_date={(self.tax_form_date if hasattr(self, "tax_form_date") else None)!r}, '
                f'additional_information={(self.additional_information if hasattr(self, "additional_information") else None)!r}, '
                f'tax_form_type={(self.tax_form_type if hasattr(self, "tax_form_type") else None)!r}, '
                f'issuer={(self.issuer if hasattr(self, "issuer") else None)!r}, '
                f'recipient={(self.recipient if hasattr(self, "recipient") else None)!r}, '
                f'attributes={(self.attributes if hasattr(self, "attributes") else None)!r}, '
                f'error={(self.error if hasattr(self, "error") else None)!r}, '
                f'links={(self.links if hasattr(self, "links") else None)!r}, '
                f'self_insured_coverage={(self.self_insured_coverage if hasattr(self, "self_insured_coverage") else None)!r}, '
                f'offers_of_coverage={(self.offers_of_coverage if hasattr(self, "offers_of_coverage") else None)!r}, '
                f'employee_age={(self.employee_age if hasattr(self, "employee_age") else None)!r}, '
                f'plan_start_month={(self.plan_start_month if hasattr(self, "plan_start_month") else None)!r}, '
                f'covered_individuals={(self.covered_individuals if hasattr(self, "covered_individuals") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'tax_year={(self.tax_year if hasattr(self, "tax_year") else None)!s}, '
                f'corrected={(self.corrected if hasattr(self, "corrected") else None)!s}, '
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!s}, '
                f'tax_form_id={(self.tax_form_id if hasattr(self, "tax_form_id") else None)!s}, '
                f'tax_form_date={(self.tax_form_date if hasattr(self, "tax_form_date") else None)!s}, '
                f'additional_information={(self.additional_information if hasattr(self, "additional_information") else None)!s}, '
                f'tax_form_type={(self.tax_form_type if hasattr(self, "tax_form_type") else None)!s}, '
                f'issuer={(self.issuer if hasattr(self, "issuer") else None)!s}, '
                f'recipient={(self.recipient if hasattr(self, "recipient") else None)!s}, '
                f'attributes={(self.attributes if hasattr(self, "attributes") else None)!s}, '
                f'error={(self.error if hasattr(self, "error") else None)!s}, '
                f'links={(self.links if hasattr(self, "links") else None)!s}, '
                f'self_insured_coverage={(self.self_insured_coverage if hasattr(self, "self_insured_coverage") else None)!s}, '
                f'offers_of_coverage={(self.offers_of_coverage if hasattr(self, "offers_of_coverage") else None)!s}, '
                f'employee_age={(self.employee_age if hasattr(self, "employee_age") else None)!s}, '
                f'plan_start_month={(self.plan_start_month if hasattr(self, "plan_start_month") else None)!s}, '
                f'covered_individuals={(self.covered_individuals if hasattr(self, "covered_individuals") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
