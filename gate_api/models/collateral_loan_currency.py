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


class CollateralLoanCurrency(object):
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
        'loan_currency': 'str',
        'collateral_currency': 'list[str]'
    }

    attribute_map = {
        'loan_currency': 'loan_currency',
        'collateral_currency': 'collateral_currency'
    }

    def __init__(self, loan_currency=None, collateral_currency=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, list[str], Configuration) -> None
        """CollateralLoanCurrency - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._loan_currency = None
        self._collateral_currency = None
        self.discriminator = None

        if loan_currency is not None:
            self.loan_currency = loan_currency
        if collateral_currency is not None:
            self.collateral_currency = collateral_currency

    @property
    def loan_currency(self):
        """Gets the loan_currency of this CollateralLoanCurrency.  # noqa: E501

        Borrowed currency  # noqa: E501

        :return: The loan_currency of this CollateralLoanCurrency.  # noqa: E501
        :rtype: str
        """
        return self._loan_currency

    @loan_currency.setter
    def loan_currency(self, loan_currency):
        """Sets the loan_currency of this CollateralLoanCurrency.

        Borrowed currency  # noqa: E501

        :param loan_currency: The loan_currency of this CollateralLoanCurrency.  # noqa: E501
        :type: str
        """

        self._loan_currency = loan_currency

    @property
    def collateral_currency(self):
        """Gets the collateral_currency of this CollateralLoanCurrency.  # noqa: E501

        List of supported collateral currencies  # noqa: E501

        :return: The collateral_currency of this CollateralLoanCurrency.  # noqa: E501
        :rtype: list[str]
        """
        return self._collateral_currency

    @collateral_currency.setter
    def collateral_currency(self, collateral_currency):
        """Sets the collateral_currency of this CollateralLoanCurrency.

        List of supported collateral currencies  # noqa: E501

        :param collateral_currency: The collateral_currency of this CollateralLoanCurrency.  # noqa: E501
        :type: list[str]
        """

        self._collateral_currency = collateral_currency

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
        if not isinstance(other, CollateralLoanCurrency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CollateralLoanCurrency):
            return True

        return self.to_dict() != other.to_dict()
