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
from akoya.models.state_and_local_tax_withholding import StateAndLocalTaxWithholding
from akoya.models.tax_form_attribute import TaxFormAttribute
from akoya.models.tax_party import TaxParty


class Form1099R(object):

    """Implementation of the 'Form 1099-R' model.

    Distributions from Pensions, Annuities, Retirement or Profit-Sharing
    Plans, IRAs, Insurance Contracts, etc.

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
        allocable_to_irr (float): Box 10, Amount allocable to IRR within 5
            years
        first_year_of_roth (int): Box 11, First year of designated Roth
            contributions. A four-digit year. (Like `TaxYear` definition, but
            lower minimum since first year of Roth IRAs was 1997)
        recipient_account_number (str): Account number
        gross_distribution (float): Box 1, Gross distribution
        taxable_amount (float): Box 2a, Taxable amount
        taxable_amount_not_determined (bool): Box 2b, Taxable amount not
            determined
        total_distribution (bool): Box 2c, Total distribution
        capital_gain (float): Box 3, Capital gain
        federal_tax_withheld (float): Box 4, Federal income tax withheld
        employee_contributions (float): Box 5, Employee contributions
        net_unrealized_appreciation (float): Box 6, Net unrealized appreciation
        distribution_codes (List[str]): Box 7, Distribution codes
        ira_sep_simple (bool): Box 7b, IRA/SEP/SIMPLE
        other_amount (float): Box 8, Other
        other_percent (float): Box 8, Other percent
        your_percent_of_total (float): Box 9a, Your percent of total
            distribution
        total_employee_contributions (float): Box 9b, Total employee
            contributions
        foreign_account_tax_compliance (bool): Box 12, FATCA filing requirement
        date_of_payment (date): Box 13, Date of payment
        state_and_local (List[StateAndLocalTaxWithholding]): Boxes 14-19,
            State and Local tax withholding
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
        "allocable_to_irr": 'allocableToIRR',
        "first_year_of_roth": 'firstYearOfRoth',
        "recipient_account_number": 'recipientAccountNumber',
        "gross_distribution": 'grossDistribution',
        "taxable_amount": 'taxableAmount',
        "taxable_amount_not_determined": 'taxableAmountNotDetermined',
        "total_distribution": 'totalDistribution',
        "capital_gain": 'capitalGain',
        "federal_tax_withheld": 'federalTaxWithheld',
        "employee_contributions": 'employeeContributions',
        "net_unrealized_appreciation": 'netUnrealizedAppreciation',
        "distribution_codes": 'distributionCodes',
        "ira_sep_simple": 'iraSepSimple',
        "other_amount": 'otherAmount',
        "other_percent": 'otherPercent',
        "your_percent_of_total": 'yourPercentOfTotal',
        "total_employee_contributions": 'totalEmployeeContributions',
        "foreign_account_tax_compliance": 'foreignAccountTaxCompliance',
        "date_of_payment": 'dateOfPayment',
        "state_and_local": 'stateAndLocal'
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
        'allocable_to_irr',
        'first_year_of_roth',
        'recipient_account_number',
        'gross_distribution',
        'taxable_amount',
        'taxable_amount_not_determined',
        'total_distribution',
        'capital_gain',
        'federal_tax_withheld',
        'employee_contributions',
        'net_unrealized_appreciation',
        'distribution_codes',
        'ira_sep_simple',
        'other_amount',
        'other_percent',
        'your_percent_of_total',
        'total_employee_contributions',
        'foreign_account_tax_compliance',
        'date_of_payment',
        'state_and_local',
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
                 allocable_to_irr=APIHelper.SKIP,
                 first_year_of_roth=APIHelper.SKIP,
                 recipient_account_number=APIHelper.SKIP,
                 gross_distribution=APIHelper.SKIP,
                 taxable_amount=APIHelper.SKIP,
                 taxable_amount_not_determined=APIHelper.SKIP,
                 total_distribution=APIHelper.SKIP,
                 capital_gain=APIHelper.SKIP,
                 federal_tax_withheld=APIHelper.SKIP,
                 employee_contributions=APIHelper.SKIP,
                 net_unrealized_appreciation=APIHelper.SKIP,
                 distribution_codes=APIHelper.SKIP,
                 ira_sep_simple=APIHelper.SKIP,
                 other_amount=APIHelper.SKIP,
                 other_percent=APIHelper.SKIP,
                 your_percent_of_total=APIHelper.SKIP,
                 total_employee_contributions=APIHelper.SKIP,
                 foreign_account_tax_compliance=APIHelper.SKIP,
                 date_of_payment=APIHelper.SKIP,
                 state_and_local=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Form1099R class"""

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
        if allocable_to_irr is not APIHelper.SKIP:
            self.allocable_to_irr = allocable_to_irr 
        if first_year_of_roth is not APIHelper.SKIP:
            self.first_year_of_roth = first_year_of_roth 
        if recipient_account_number is not APIHelper.SKIP:
            self.recipient_account_number = recipient_account_number 
        if gross_distribution is not APIHelper.SKIP:
            self.gross_distribution = gross_distribution 
        if taxable_amount is not APIHelper.SKIP:
            self.taxable_amount = taxable_amount 
        if taxable_amount_not_determined is not APIHelper.SKIP:
            self.taxable_amount_not_determined = taxable_amount_not_determined 
        if total_distribution is not APIHelper.SKIP:
            self.total_distribution = total_distribution 
        if capital_gain is not APIHelper.SKIP:
            self.capital_gain = capital_gain 
        if federal_tax_withheld is not APIHelper.SKIP:
            self.federal_tax_withheld = federal_tax_withheld 
        if employee_contributions is not APIHelper.SKIP:
            self.employee_contributions = employee_contributions 
        if net_unrealized_appreciation is not APIHelper.SKIP:
            self.net_unrealized_appreciation = net_unrealized_appreciation 
        if distribution_codes is not APIHelper.SKIP:
            self.distribution_codes = distribution_codes 
        if ira_sep_simple is not APIHelper.SKIP:
            self.ira_sep_simple = ira_sep_simple 
        if other_amount is not APIHelper.SKIP:
            self.other_amount = other_amount 
        if other_percent is not APIHelper.SKIP:
            self.other_percent = other_percent 
        if your_percent_of_total is not APIHelper.SKIP:
            self.your_percent_of_total = your_percent_of_total 
        if total_employee_contributions is not APIHelper.SKIP:
            self.total_employee_contributions = total_employee_contributions 
        if foreign_account_tax_compliance is not APIHelper.SKIP:
            self.foreign_account_tax_compliance = foreign_account_tax_compliance 
        if date_of_payment is not APIHelper.SKIP:
            self.date_of_payment = date_of_payment 
        if state_and_local is not APIHelper.SKIP:
            self.state_and_local = state_and_local 

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
        allocable_to_irr = dictionary.get("allocableToIRR") if dictionary.get("allocableToIRR") else APIHelper.SKIP
        first_year_of_roth = dictionary.get("firstYearOfRoth") if dictionary.get("firstYearOfRoth") else APIHelper.SKIP
        recipient_account_number = dictionary.get("recipientAccountNumber") if dictionary.get("recipientAccountNumber") else APIHelper.SKIP
        gross_distribution = dictionary.get("grossDistribution") if dictionary.get("grossDistribution") else APIHelper.SKIP
        taxable_amount = dictionary.get("taxableAmount") if dictionary.get("taxableAmount") else APIHelper.SKIP
        taxable_amount_not_determined = dictionary.get("taxableAmountNotDetermined") if "taxableAmountNotDetermined" in dictionary.keys() else APIHelper.SKIP
        total_distribution = dictionary.get("totalDistribution") if "totalDistribution" in dictionary.keys() else APIHelper.SKIP
        capital_gain = dictionary.get("capitalGain") if dictionary.get("capitalGain") else APIHelper.SKIP
        federal_tax_withheld = dictionary.get("federalTaxWithheld") if dictionary.get("federalTaxWithheld") else APIHelper.SKIP
        employee_contributions = dictionary.get("employeeContributions") if dictionary.get("employeeContributions") else APIHelper.SKIP
        net_unrealized_appreciation = dictionary.get("netUnrealizedAppreciation") if dictionary.get("netUnrealizedAppreciation") else APIHelper.SKIP
        distribution_codes = dictionary.get("distributionCodes") if dictionary.get("distributionCodes") else APIHelper.SKIP
        ira_sep_simple = dictionary.get("iraSepSimple") if "iraSepSimple" in dictionary.keys() else APIHelper.SKIP
        other_amount = dictionary.get("otherAmount") if dictionary.get("otherAmount") else APIHelper.SKIP
        other_percent = dictionary.get("otherPercent") if dictionary.get("otherPercent") else APIHelper.SKIP
        your_percent_of_total = dictionary.get("yourPercentOfTotal") if dictionary.get("yourPercentOfTotal") else APIHelper.SKIP
        total_employee_contributions = dictionary.get("totalEmployeeContributions") if dictionary.get("totalEmployeeContributions") else APIHelper.SKIP
        foreign_account_tax_compliance = dictionary.get("foreignAccountTaxCompliance") if "foreignAccountTaxCompliance" in dictionary.keys() else APIHelper.SKIP
        date_of_payment = dateutil.parser.parse(dictionary.get('dateOfPayment')).date() if dictionary.get('dateOfPayment') else APIHelper.SKIP
        state_and_local = None
        if dictionary.get('stateAndLocal') is not None:
            state_and_local = [StateAndLocalTaxWithholding.from_dictionary(x) for x in dictionary.get('stateAndLocal')]
        else:
            state_and_local = APIHelper.SKIP
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
                   allocable_to_irr,
                   first_year_of_roth,
                   recipient_account_number,
                   gross_distribution,
                   taxable_amount,
                   taxable_amount_not_determined,
                   total_distribution,
                   capital_gain,
                   federal_tax_withheld,
                   employee_contributions,
                   net_unrealized_appreciation,
                   distribution_codes,
                   ira_sep_simple,
                   other_amount,
                   other_percent,
                   your_percent_of_total,
                   total_employee_contributions,
                   foreign_account_tax_compliance,
                   date_of_payment,
                   state_and_local,
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
                f'allocable_to_irr={(self.allocable_to_irr if hasattr(self, "allocable_to_irr") else None)!r}, '
                f'first_year_of_roth={(self.first_year_of_roth if hasattr(self, "first_year_of_roth") else None)!r}, '
                f'recipient_account_number={(self.recipient_account_number if hasattr(self, "recipient_account_number") else None)!r}, '
                f'gross_distribution={(self.gross_distribution if hasattr(self, "gross_distribution") else None)!r}, '
                f'taxable_amount={(self.taxable_amount if hasattr(self, "taxable_amount") else None)!r}, '
                f'taxable_amount_not_determined={(self.taxable_amount_not_determined if hasattr(self, "taxable_amount_not_determined") else None)!r}, '
                f'total_distribution={(self.total_distribution if hasattr(self, "total_distribution") else None)!r}, '
                f'capital_gain={(self.capital_gain if hasattr(self, "capital_gain") else None)!r}, '
                f'federal_tax_withheld={(self.federal_tax_withheld if hasattr(self, "federal_tax_withheld") else None)!r}, '
                f'employee_contributions={(self.employee_contributions if hasattr(self, "employee_contributions") else None)!r}, '
                f'net_unrealized_appreciation={(self.net_unrealized_appreciation if hasattr(self, "net_unrealized_appreciation") else None)!r}, '
                f'distribution_codes={(self.distribution_codes if hasattr(self, "distribution_codes") else None)!r}, '
                f'ira_sep_simple={(self.ira_sep_simple if hasattr(self, "ira_sep_simple") else None)!r}, '
                f'other_amount={(self.other_amount if hasattr(self, "other_amount") else None)!r}, '
                f'other_percent={(self.other_percent if hasattr(self, "other_percent") else None)!r}, '
                f'your_percent_of_total={(self.your_percent_of_total if hasattr(self, "your_percent_of_total") else None)!r}, '
                f'total_employee_contributions={(self.total_employee_contributions if hasattr(self, "total_employee_contributions") else None)!r}, '
                f'foreign_account_tax_compliance={(self.foreign_account_tax_compliance if hasattr(self, "foreign_account_tax_compliance") else None)!r}, '
                f'date_of_payment={(self.date_of_payment if hasattr(self, "date_of_payment") else None)!r}, '
                f'state_and_local={(self.state_and_local if hasattr(self, "state_and_local") else None)!r}, '
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
                f'allocable_to_irr={(self.allocable_to_irr if hasattr(self, "allocable_to_irr") else None)!s}, '
                f'first_year_of_roth={(self.first_year_of_roth if hasattr(self, "first_year_of_roth") else None)!s}, '
                f'recipient_account_number={(self.recipient_account_number if hasattr(self, "recipient_account_number") else None)!s}, '
                f'gross_distribution={(self.gross_distribution if hasattr(self, "gross_distribution") else None)!s}, '
                f'taxable_amount={(self.taxable_amount if hasattr(self, "taxable_amount") else None)!s}, '
                f'taxable_amount_not_determined={(self.taxable_amount_not_determined if hasattr(self, "taxable_amount_not_determined") else None)!s}, '
                f'total_distribution={(self.total_distribution if hasattr(self, "total_distribution") else None)!s}, '
                f'capital_gain={(self.capital_gain if hasattr(self, "capital_gain") else None)!s}, '
                f'federal_tax_withheld={(self.federal_tax_withheld if hasattr(self, "federal_tax_withheld") else None)!s}, '
                f'employee_contributions={(self.employee_contributions if hasattr(self, "employee_contributions") else None)!s}, '
                f'net_unrealized_appreciation={(self.net_unrealized_appreciation if hasattr(self, "net_unrealized_appreciation") else None)!s}, '
                f'distribution_codes={(self.distribution_codes if hasattr(self, "distribution_codes") else None)!s}, '
                f'ira_sep_simple={(self.ira_sep_simple if hasattr(self, "ira_sep_simple") else None)!s}, '
                f'other_amount={(self.other_amount if hasattr(self, "other_amount") else None)!s}, '
                f'other_percent={(self.other_percent if hasattr(self, "other_percent") else None)!s}, '
                f'your_percent_of_total={(self.your_percent_of_total if hasattr(self, "your_percent_of_total") else None)!s}, '
                f'total_employee_contributions={(self.total_employee_contributions if hasattr(self, "total_employee_contributions") else None)!s}, '
                f'foreign_account_tax_compliance={(self.foreign_account_tax_compliance if hasattr(self, "foreign_account_tax_compliance") else None)!s}, '
                f'date_of_payment={(self.date_of_payment if hasattr(self, "date_of_payment") else None)!s}, '
                f'state_and_local={(self.state_and_local if hasattr(self, "state_and_local") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
