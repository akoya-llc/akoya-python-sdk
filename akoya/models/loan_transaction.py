# -*- coding: utf-8 -*-

"""
akoya

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from akoya.api_helper import APIHelper
from akoya.models.fi_attribute_entity import FiAttributeEntity
from akoya.models.hateoas_link import HateoasLink
from akoya.models.line_item import LineItem
from akoya.models.payment_details import PaymentDetails


class LoanTransaction(object):

    """Implementation of the 'Loan Transaction' model.

    Loan Transaction

    Attributes:
        account_id (str): Corresponds to AccountId in Account
        amount (float): The amount of money in the account currency.  If
            balanceType is `ASSET`:    1. If `debitCreditMemo` = `DEBIT`, sign
            is "+" or not present   2. If `CREDIT`, sign is "-"  If
            balanceType is `LIABILITY`:    1. If `debitCreditMemo` = `DEBIT`,
            sign is "-"   2. If `CREDIT`, sign is "+" or not present
        category (str): Transaction category, preferably MCC or SIC.
        debit_credit_memo (DebitCreditMemo): Akoya will ensure that this is
            correctly populated with one of DEBIT or CREDIT and matches the
            sign of the status field.
        description (str): The description of the transaction
        image_ids (List[str]): Array of image identifiers (unique to
            transaction) used to retrieve images of check or transaction
            receipt.
        fi_attributes (List[FiAttributeEntity]): Array of FI-specific
            attributes
        foreign_amount (float): The amount of money in the foreign currency
        foreign_currency (str): The ISO 4217 code of the foreign currency
        line_item (List[LineItem]): Breakdown of the transaction details
        links (List[HateoasLink]): Links (unique to this Transaction) used to
            retrieve images of checks or transaction receipts, or invoke other
            APIs
        memo (str): Secondary transaction description
        posted_timestamp (datetime): The date and time that the transaction
            was posted to the account. If not provided then
            TransactionTimestamp can be used as PostedTimeStamp.
        reference (str): A tracking reference identifier
        reference_transaction_id (str): Akoya ensures that this field is
            populated for all transactions which are reversals, otherwise it
            is null. Either way it is always present.  For reverse postings,
            the identity of the transaction being reversed. For the correction
            transaction, the identity of the reversing post. For credit card
            posting transactions, the identity of the authorization
            transaction.
        status (TransationStatus): AUTHORIZATION, MEMO, PENDING, or POSTED
        sub_category (str): Transaction category detail
        transaction_id (str): Long term persistent identity of the transaction
            (unique to account).  Transaction IDs should:     1. be the same
            for pending and posted    2. be different for reversed
            transactions    3. `referenceTransactionId` should be present for
            reversed transactions'
        transaction_timestamp (datetime): The date and time that the
            transaction was added to the server backend systems.  Akoya
            ensures that this field is populated for all transactions to which
            it applies, otherwise it is null. Either way it is always present.
        payment_details (PaymentDetails): Payment details for some transactions
        transaction_type (LoanTransactionType): LoanTransaction Type
        additional_properties (Dict[str, Any]): The additional properties for
            the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id": 'accountId',
        "amount": 'amount',
        "category": 'category',
        "debit_credit_memo": 'debitCreditMemo',
        "description": 'description',
        "image_ids": 'imageIds',
        "fi_attributes": 'fiAttributes',
        "foreign_amount": 'foreignAmount',
        "foreign_currency": 'foreignCurrency',
        "line_item": 'lineItem',
        "links": 'links',
        "memo": 'memo',
        "posted_timestamp": 'postedTimestamp',
        "reference": 'reference',
        "reference_transaction_id": 'referenceTransactionId',
        "status": 'status',
        "sub_category": 'subCategory',
        "transaction_id": 'transactionId',
        "transaction_timestamp": 'transactionTimestamp',
        "payment_details": 'paymentDetails',
        "transaction_type": 'transactionType'
    }

    _optionals = [
        'account_id',
        'amount',
        'category',
        'debit_credit_memo',
        'description',
        'image_ids',
        'fi_attributes',
        'foreign_amount',
        'foreign_currency',
        'line_item',
        'links',
        'memo',
        'posted_timestamp',
        'reference',
        'reference_transaction_id',
        'status',
        'sub_category',
        'transaction_id',
        'transaction_timestamp',
        'payment_details',
        'transaction_type',
    ]

    def __init__(self,
                 account_id=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 category=APIHelper.SKIP,
                 debit_credit_memo=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 image_ids=APIHelper.SKIP,
                 fi_attributes=APIHelper.SKIP,
                 foreign_amount=APIHelper.SKIP,
                 foreign_currency=APIHelper.SKIP,
                 line_item=APIHelper.SKIP,
                 links=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 posted_timestamp=APIHelper.SKIP,
                 reference=APIHelper.SKIP,
                 reference_transaction_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 sub_category=APIHelper.SKIP,
                 transaction_id=APIHelper.SKIP,
                 transaction_timestamp=APIHelper.SKIP,
                 payment_details=APIHelper.SKIP,
                 transaction_type=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the LoanTransaction class"""

        # Initialize members of the class
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if category is not APIHelper.SKIP:
            self.category = category 
        if debit_credit_memo is not APIHelper.SKIP:
            self.debit_credit_memo = debit_credit_memo 
        if description is not APIHelper.SKIP:
            self.description = description 
        if image_ids is not APIHelper.SKIP:
            self.image_ids = image_ids 
        if fi_attributes is not APIHelper.SKIP:
            self.fi_attributes = fi_attributes 
        if foreign_amount is not APIHelper.SKIP:
            self.foreign_amount = foreign_amount 
        if foreign_currency is not APIHelper.SKIP:
            self.foreign_currency = foreign_currency 
        if line_item is not APIHelper.SKIP:
            self.line_item = line_item 
        if links is not APIHelper.SKIP:
            self.links = links 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if posted_timestamp is not APIHelper.SKIP:
            self.posted_timestamp = APIHelper.apply_datetime_converter(posted_timestamp, APIHelper.RFC3339DateTime) if posted_timestamp else None 
        if reference is not APIHelper.SKIP:
            self.reference = reference 
        if reference_transaction_id is not APIHelper.SKIP:
            self.reference_transaction_id = reference_transaction_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if sub_category is not APIHelper.SKIP:
            self.sub_category = sub_category 
        if transaction_id is not APIHelper.SKIP:
            self.transaction_id = transaction_id 
        if transaction_timestamp is not APIHelper.SKIP:
            self.transaction_timestamp = APIHelper.apply_datetime_converter(transaction_timestamp, APIHelper.RFC3339DateTime) if transaction_timestamp else None 
        if payment_details is not APIHelper.SKIP:
            self.payment_details = payment_details 
        if transaction_type is not APIHelper.SKIP:
            self.transaction_type = transaction_type 

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
        account_id = dictionary.get("accountId") if dictionary.get("accountId") else APIHelper.SKIP
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        category = dictionary.get("category") if dictionary.get("category") else APIHelper.SKIP
        debit_credit_memo = dictionary.get("debitCreditMemo") if dictionary.get("debitCreditMemo") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        image_ids = dictionary.get("imageIds") if dictionary.get("imageIds") else APIHelper.SKIP
        fi_attributes = None
        if dictionary.get('fiAttributes') is not None:
            fi_attributes = [FiAttributeEntity.from_dictionary(x) for x in dictionary.get('fiAttributes')]
        else:
            fi_attributes = APIHelper.SKIP
        foreign_amount = dictionary.get("foreignAmount") if dictionary.get("foreignAmount") else APIHelper.SKIP
        foreign_currency = dictionary.get("foreignCurrency") if dictionary.get("foreignCurrency") else APIHelper.SKIP
        line_item = None
        if dictionary.get('lineItem') is not None:
            line_item = [LineItem.from_dictionary(x) for x in dictionary.get('lineItem')]
        else:
            line_item = APIHelper.SKIP
        links = None
        if dictionary.get('links') is not None:
            links = [HateoasLink.from_dictionary(x) for x in dictionary.get('links')]
        else:
            links = APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        posted_timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("postedTimestamp")).datetime if dictionary.get("postedTimestamp") else APIHelper.SKIP
        reference = dictionary.get("reference") if dictionary.get("reference") else APIHelper.SKIP
        reference_transaction_id = dictionary.get("referenceTransactionId") if dictionary.get("referenceTransactionId") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        sub_category = dictionary.get("subCategory") if dictionary.get("subCategory") else APIHelper.SKIP
        transaction_id = dictionary.get("transactionId") if dictionary.get("transactionId") else APIHelper.SKIP
        transaction_timestamp = APIHelper.RFC3339DateTime.from_value(dictionary.get("transactionTimestamp")).datetime if dictionary.get("transactionTimestamp") else APIHelper.SKIP
        payment_details = PaymentDetails.from_dictionary(dictionary.get('paymentDetails')) if 'paymentDetails' in dictionary.keys() else APIHelper.SKIP
        transaction_type = dictionary.get("transactionType") if dictionary.get("transactionType") else APIHelper.SKIP
        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items() if k not in cls._names.values()},
            unboxing_function=lambda value: value)
        # Return an object of this model
        return cls(account_id,
                   amount,
                   category,
                   debit_credit_memo,
                   description,
                   image_ids,
                   fi_attributes,
                   foreign_amount,
                   foreign_currency,
                   line_item,
                   links,
                   memo,
                   posted_timestamp,
                   reference,
                   reference_transaction_id,
                   status,
                   sub_category,
                   transaction_id,
                   transaction_timestamp,
                   payment_details,
                   transaction_type,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!r}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!r}, '
                f'category={(self.category if hasattr(self, "category") else None)!r}, '
                f'debit_credit_memo={(self.debit_credit_memo if hasattr(self, "debit_credit_memo") else None)!r}, '
                f'description={(self.description if hasattr(self, "description") else None)!r}, '
                f'image_ids={(self.image_ids if hasattr(self, "image_ids") else None)!r}, '
                f'fi_attributes={(self.fi_attributes if hasattr(self, "fi_attributes") else None)!r}, '
                f'foreign_amount={(self.foreign_amount if hasattr(self, "foreign_amount") else None)!r}, '
                f'foreign_currency={(self.foreign_currency if hasattr(self, "foreign_currency") else None)!r}, '
                f'line_item={(self.line_item if hasattr(self, "line_item") else None)!r}, '
                f'links={(self.links if hasattr(self, "links") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'posted_timestamp={(self.posted_timestamp if hasattr(self, "posted_timestamp") else None)!r}, '
                f'reference={(self.reference if hasattr(self, "reference") else None)!r}, '
                f'reference_transaction_id={(self.reference_transaction_id if hasattr(self, "reference_transaction_id") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'sub_category={(self.sub_category if hasattr(self, "sub_category") else None)!r}, '
                f'transaction_id={(self.transaction_id if hasattr(self, "transaction_id") else None)!r}, '
                f'transaction_timestamp={(self.transaction_timestamp if hasattr(self, "transaction_timestamp") else None)!r}, '
                f'payment_details={(self.payment_details if hasattr(self, "payment_details") else None)!r}, '
                f'transaction_type={(self.transaction_type if hasattr(self, "transaction_type") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!s}, '
                f'amount={(self.amount if hasattr(self, "amount") else None)!s}, '
                f'category={(self.category if hasattr(self, "category") else None)!s}, '
                f'debit_credit_memo={(self.debit_credit_memo if hasattr(self, "debit_credit_memo") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s}, '
                f'image_ids={(self.image_ids if hasattr(self, "image_ids") else None)!s}, '
                f'fi_attributes={(self.fi_attributes if hasattr(self, "fi_attributes") else None)!s}, '
                f'foreign_amount={(self.foreign_amount if hasattr(self, "foreign_amount") else None)!s}, '
                f'foreign_currency={(self.foreign_currency if hasattr(self, "foreign_currency") else None)!s}, '
                f'line_item={(self.line_item if hasattr(self, "line_item") else None)!s}, '
                f'links={(self.links if hasattr(self, "links") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'posted_timestamp={(self.posted_timestamp if hasattr(self, "posted_timestamp") else None)!s}, '
                f'reference={(self.reference if hasattr(self, "reference") else None)!s}, '
                f'reference_transaction_id={(self.reference_transaction_id if hasattr(self, "reference_transaction_id") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'sub_category={(self.sub_category if hasattr(self, "sub_category") else None)!s}, '
                f'transaction_id={(self.transaction_id if hasattr(self, "transaction_id") else None)!s}, '
                f'transaction_timestamp={(self.transaction_timestamp if hasattr(self, "transaction_timestamp") else None)!s}, '
                f'payment_details={(self.payment_details if hasattr(self, "payment_details") else None)!s}, '
                f'transaction_type={(self.transaction_type if hasattr(self, "transaction_type") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
