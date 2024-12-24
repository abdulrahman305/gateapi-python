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


class AccountBalance(object):
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
        'amount': 'str',
        'currency': 'str',
        'unrealised_pnl': 'str',
        'borrowed': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency',
        'unrealised_pnl': 'unrealised_pnl',
        'borrowed': 'borrowed'
    }

    def __init__(self, amount=None, currency=None, unrealised_pnl=None, borrowed=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, str, str, Configuration) -> None
        """AccountBalance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._currency = None
        self._unrealised_pnl = None
        self._borrowed = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if unrealised_pnl is not None:
            self.unrealised_pnl = unrealised_pnl
        if borrowed is not None:
            self.borrowed = borrowed

    @property
    def amount(self):
        """Gets the amount of this AccountBalance.  # noqa: E501

        Account total balance amount  # noqa: E501

        :return: The amount of this AccountBalance.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AccountBalance.

        Account total balance amount  # noqa: E501

        :param amount: The amount of this AccountBalance.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this AccountBalance.  # noqa: E501

        Currency  # noqa: E501

        :return: The currency of this AccountBalance.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AccountBalance.

        Currency  # noqa: E501

        :param currency: The currency of this AccountBalance.  # noqa: E501
        :type: str
        """
        allowed_values = ["BTC", "CNY", "USD", "USDT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and currency not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def unrealised_pnl(self):
        """Gets the unrealised_pnl of this AccountBalance.  # noqa: E501

        Unrealised_pnl, this field will only appear in futures, options, delivery, and total accounts  # noqa: E501

        :return: The unrealised_pnl of this AccountBalance.  # noqa: E501
        :rtype: str
        """
        return self._unrealised_pnl

    @unrealised_pnl.setter
    def unrealised_pnl(self, unrealised_pnl):
        """Sets the unrealised_pnl of this AccountBalance.

        Unrealised_pnl, this field will only appear in futures, options, delivery, and total accounts  # noqa: E501

        :param unrealised_pnl: The unrealised_pnl of this AccountBalance.  # noqa: E501
        :type: str
        """

        self._unrealised_pnl = unrealised_pnl

    @property
    def borrowed(self):
        """Gets the borrowed of this AccountBalance.  # noqa: E501

        Borrowed，this field will only appear in margin and cross_margin accounts  # noqa: E501

        :return: The borrowed of this AccountBalance.  # noqa: E501
        :rtype: str
        """
        return self._borrowed

    @borrowed.setter
    def borrowed(self, borrowed):
        """Sets the borrowed of this AccountBalance.

        Borrowed，this field will only appear in margin and cross_margin accounts  # noqa: E501

        :param borrowed: The borrowed of this AccountBalance.  # noqa: E501
        :type: str
        """

        self._borrowed = borrowed

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
        if not isinstance(other, AccountBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountBalance):
            return True

        return self.to_dict() != other.to_dict()
