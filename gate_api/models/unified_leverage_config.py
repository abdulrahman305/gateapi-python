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


class UnifiedLeverageConfig(object):
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
        'current_leverage': 'str',
        'min_leverage': 'str',
        'max_leverage': 'str',
        'debit': 'str',
        'available_margin': 'str',
        'borrowable': 'str',
        'except_leverage_borrowable': 'str'
    }

    attribute_map = {
        'current_leverage': 'current_leverage',
        'min_leverage': 'min_leverage',
        'max_leverage': 'max_leverage',
        'debit': 'debit',
        'available_margin': 'available_margin',
        'borrowable': 'borrowable',
        'except_leverage_borrowable': 'except_leverage_borrowable'
    }

    def __init__(self, current_leverage=None, min_leverage=None, max_leverage=None, debit=None, available_margin=None, borrowable=None, except_leverage_borrowable=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, str, str, str, str, str, Configuration) -> None
        """UnifiedLeverageConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._current_leverage = None
        self._min_leverage = None
        self._max_leverage = None
        self._debit = None
        self._available_margin = None
        self._borrowable = None
        self._except_leverage_borrowable = None
        self.discriminator = None

        if current_leverage is not None:
            self.current_leverage = current_leverage
        if min_leverage is not None:
            self.min_leverage = min_leverage
        if max_leverage is not None:
            self.max_leverage = max_leverage
        if debit is not None:
            self.debit = debit
        if available_margin is not None:
            self.available_margin = available_margin
        if borrowable is not None:
            self.borrowable = borrowable
        if except_leverage_borrowable is not None:
            self.except_leverage_borrowable = except_leverage_borrowable

    @property
    def current_leverage(self):
        """Gets the current_leverage of this UnifiedLeverageConfig.  # noqa: E501

        Current leverage ratio  # noqa: E501

        :return: The current_leverage of this UnifiedLeverageConfig.  # noqa: E501
        :rtype: str
        """
        return self._current_leverage

    @current_leverage.setter
    def current_leverage(self, current_leverage):
        """Sets the current_leverage of this UnifiedLeverageConfig.

        Current leverage ratio  # noqa: E501

        :param current_leverage: The current_leverage of this UnifiedLeverageConfig.  # noqa: E501
        :type: str
        """

        self._current_leverage = current_leverage

    @property
    def min_leverage(self):
        """Gets the min_leverage of this UnifiedLeverageConfig.  # noqa: E501

        Minimum adjustable leverage ratio  # noqa: E501

        :return: The min_leverage of this UnifiedLeverageConfig.  # noqa: E501
        :rtype: str
        """
        return self._min_leverage

    @min_leverage.setter
    def min_leverage(self, min_leverage):
        """Sets the min_leverage of this UnifiedLeverageConfig.

        Minimum adjustable leverage ratio  # noqa: E501

        :param min_leverage: The min_leverage of this UnifiedLeverageConfig.  # noqa: E501
        :type: str
        """

        self._min_leverage = min_leverage

    @property
    def max_leverage(self):
        """Gets the max_leverage of this UnifiedLeverageConfig.  # noqa: E501

        Maximum adjustable leverage ratio  # noqa: E501

        :return: The max_leverage of this UnifiedLeverageConfig.  # noqa: E501
        :rtype: str
        """
        return self._max_leverage

    @max_leverage.setter
    def max_leverage(self, max_leverage):
        """Sets the max_leverage of this UnifiedLeverageConfig.

        Maximum adjustable leverage ratio  # noqa: E501

        :param max_leverage: The max_leverage of this UnifiedLeverageConfig.  # noqa: E501
        :type: str
        """

        self._max_leverage = max_leverage

    @property
    def debit(self):
        """Gets the debit of this UnifiedLeverageConfig.  # noqa: E501

        Current liabilities  # noqa: E501

        :return: The debit of this UnifiedLeverageConfig.  # noqa: E501
        :rtype: str
        """
        return self._debit

    @debit.setter
    def debit(self, debit):
        """Sets the debit of this UnifiedLeverageConfig.

        Current liabilities  # noqa: E501

        :param debit: The debit of this UnifiedLeverageConfig.  # noqa: E501
        :type: str
        """

        self._debit = debit

    @property
    def available_margin(self):
        """Gets the available_margin of this UnifiedLeverageConfig.  # noqa: E501

        Available Margin  # noqa: E501

        :return: The available_margin of this UnifiedLeverageConfig.  # noqa: E501
        :rtype: str
        """
        return self._available_margin

    @available_margin.setter
    def available_margin(self, available_margin):
        """Sets the available_margin of this UnifiedLeverageConfig.

        Available Margin  # noqa: E501

        :param available_margin: The available_margin of this UnifiedLeverageConfig.  # noqa: E501
        :type: str
        """

        self._available_margin = available_margin

    @property
    def borrowable(self):
        """Gets the borrowable of this UnifiedLeverageConfig.  # noqa: E501

        The current leverage you can choose is  # noqa: E501

        :return: The borrowable of this UnifiedLeverageConfig.  # noqa: E501
        :rtype: str
        """
        return self._borrowable

    @borrowable.setter
    def borrowable(self, borrowable):
        """Sets the borrowable of this UnifiedLeverageConfig.

        The current leverage you can choose is  # noqa: E501

        :param borrowable: The borrowable of this UnifiedLeverageConfig.  # noqa: E501
        :type: str
        """

        self._borrowable = borrowable

    @property
    def except_leverage_borrowable(self):
        """Gets the except_leverage_borrowable of this UnifiedLeverageConfig.  # noqa: E501

        The maximum amount of margin that can be borrowed and the maximum amount of Yubibao that can be borrowed, whichever is smaller  # noqa: E501

        :return: The except_leverage_borrowable of this UnifiedLeverageConfig.  # noqa: E501
        :rtype: str
        """
        return self._except_leverage_borrowable

    @except_leverage_borrowable.setter
    def except_leverage_borrowable(self, except_leverage_borrowable):
        """Sets the except_leverage_borrowable of this UnifiedLeverageConfig.

        The maximum amount of margin that can be borrowed and the maximum amount of Yubibao that can be borrowed, whichever is smaller  # noqa: E501

        :param except_leverage_borrowable: The except_leverage_borrowable of this UnifiedLeverageConfig.  # noqa: E501
        :type: str
        """

        self._except_leverage_borrowable = except_leverage_borrowable

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
        if not isinstance(other, UnifiedLeverageConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnifiedLeverageConfig):
            return True

        return self.to_dict() != other.to_dict()
