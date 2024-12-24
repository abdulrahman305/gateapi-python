# coding: utf-8

"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gate_api.configuration import Configuration


class LoanPatch(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'currency': 'str',
        'side': 'str',
        'auto_renew': 'bool',
        'currency_pair': 'str',
        'loan_id': 'str'
    }

    attribute_map = {
        'currency': 'currency',
        'side': 'side',
        'auto_renew': 'auto_renew',
        'currency_pair': 'currency_pair',
        'loan_id': 'loan_id'
    }

    def __init__(self, currency=None, side=None, auto_renew=None, currency_pair=None, loan_id=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, bool, str, str, Configuration) -> None
        """LoanPatch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency = None
        self._side = None
        self._auto_renew = None
        self._currency_pair = None
        self._loan_id = None
        self.discriminator = None

        self.currency = currency
        self.side = side
        self.auto_renew = auto_renew
        if currency_pair is not None:
            self.currency_pair = currency_pair
        if loan_id is not None:
            self.loan_id = loan_id

    @property
    def currency(self):
        """Gets the currency of this LoanPatch.  # noqa: E501

        Loan currency  # noqa: E501

        :return: The currency of this LoanPatch.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this LoanPatch.

        Loan currency  # noqa: E501

        :param currency: The currency of this LoanPatch.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def side(self):
        """Gets the side of this LoanPatch.  # noqa: E501

        Loan side. Possible values are `lend` and `borrow`. For `LoanRecord` patching, only `lend` is supported  # noqa: E501

        :return: The side of this LoanPatch.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this LoanPatch.

        Loan side. Possible values are `lend` and `borrow`. For `LoanRecord` patching, only `lend` is supported  # noqa: E501

        :param side: The side of this LoanPatch.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and side is None:  # noqa: E501
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501
        allowed_values = ["lend", "borrow"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and side not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `side` ({0}), must be one of {1}"  # noqa: E501
                .format(side, allowed_values)
            )

        self._side = side

    @property
    def auto_renew(self):
        """Gets the auto_renew of this LoanPatch.  # noqa: E501

        Auto renew  # noqa: E501

        :return: The auto_renew of this LoanPatch.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this LoanPatch.

        Auto renew  # noqa: E501

        :param auto_renew: The auto_renew of this LoanPatch.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and auto_renew is None:  # noqa: E501
            raise ValueError("Invalid value for `auto_renew`, must not be `None`")  # noqa: E501

        self._auto_renew = auto_renew

    @property
    def currency_pair(self):
        """Gets the currency_pair of this LoanPatch.  # noqa: E501

        Currency pair. Required if borrowing  # noqa: E501

        :return: The currency_pair of this LoanPatch.  # noqa: E501
        :rtype: str
        """
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, currency_pair):
        """Sets the currency_pair of this LoanPatch.

        Currency pair. Required if borrowing  # noqa: E501

        :param currency_pair: The currency_pair of this LoanPatch.  # noqa: E501
        :type: str
        """

        self._currency_pair = currency_pair

    @property
    def loan_id(self):
        """Gets the loan_id of this LoanPatch.  # noqa: E501

        Loan ID. Required for `LoanRecord` patching  # noqa: E501

        :return: The loan_id of this LoanPatch.  # noqa: E501
        :rtype: str
        """
        return self._loan_id

    @loan_id.setter
    def loan_id(self, loan_id):
        """Sets the loan_id of this LoanPatch.

        Loan ID. Required for `LoanRecord` patching  # noqa: E501

        :param loan_id: The loan_id of this LoanPatch.  # noqa: E501
        :type: str
        """

        self._loan_id = loan_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LoanPatch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoanPatch):
            return True

        return self.to_dict() != other.to_dict()
