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


class UniInterestRecord(object):
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
        'status': 'int',
        'currency': 'str',
        'actual_rate': 'str',
        'interest': 'str',
        'interest_status': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'status': 'status',
        'currency': 'currency',
        'actual_rate': 'actual_rate',
        'interest': 'interest',
        'interest_status': 'interest_status',
        'create_time': 'create_time'
    }

    def __init__(self, status=None, currency=None, actual_rate=None, interest=None, interest_status=None, create_time=None, local_vars_configuration=None):  # noqa: E501
        # type: (int, str, str, str, str, int, Configuration) -> None
        """UniInterestRecord - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._currency = None
        self._actual_rate = None
        self._interest = None
        self._interest_status = None
        self._create_time = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if currency is not None:
            self.currency = currency
        if actual_rate is not None:
            self.actual_rate = actual_rate
        if interest is not None:
            self.interest = interest
        if interest_status is not None:
            self.interest_status = interest_status
        if create_time is not None:
            self.create_time = create_time

    @property
    def status(self):
        """Gets the status of this UniInterestRecord.  # noqa: E501

        Status: 0 - fail, 1 - success  # noqa: E501

        :return: The status of this UniInterestRecord.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UniInterestRecord.

        Status: 0 - fail, 1 - success  # noqa: E501

        :param status: The status of this UniInterestRecord.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def currency(self):
        """Gets the currency of this UniInterestRecord.  # noqa: E501

        Currency  # noqa: E501

        :return: The currency of this UniInterestRecord.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this UniInterestRecord.

        Currency  # noqa: E501

        :param currency: The currency of this UniInterestRecord.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def actual_rate(self):
        """Gets the actual_rate of this UniInterestRecord.  # noqa: E501

        Actual Rate  # noqa: E501

        :return: The actual_rate of this UniInterestRecord.  # noqa: E501
        :rtype: str
        """
        return self._actual_rate

    @actual_rate.setter
    def actual_rate(self, actual_rate):
        """Sets the actual_rate of this UniInterestRecord.

        Actual Rate  # noqa: E501

        :param actual_rate: The actual_rate of this UniInterestRecord.  # noqa: E501
        :type: str
        """

        self._actual_rate = actual_rate

    @property
    def interest(self):
        """Gets the interest of this UniInterestRecord.  # noqa: E501

        Interest  # noqa: E501

        :return: The interest of this UniInterestRecord.  # noqa: E501
        :rtype: str
        """
        return self._interest

    @interest.setter
    def interest(self, interest):
        """Sets the interest of this UniInterestRecord.

        Interest  # noqa: E501

        :param interest: The interest of this UniInterestRecord.  # noqa: E501
        :type: str
        """

        self._interest = interest

    @property
    def interest_status(self):
        """Gets the interest_status of this UniInterestRecord.  # noqa: E501

        Interest status: interest_dividend - regular dividend, interest_reinvest - interest reinvestment  # noqa: E501

        :return: The interest_status of this UniInterestRecord.  # noqa: E501
        :rtype: str
        """
        return self._interest_status

    @interest_status.setter
    def interest_status(self, interest_status):
        """Sets the interest_status of this UniInterestRecord.

        Interest status: interest_dividend - regular dividend, interest_reinvest - interest reinvestment  # noqa: E501

        :param interest_status: The interest_status of this UniInterestRecord.  # noqa: E501
        :type: str
        """

        self._interest_status = interest_status

    @property
    def create_time(self):
        """Gets the create_time of this UniInterestRecord.  # noqa: E501

        Created time  # noqa: E501

        :return: The create_time of this UniInterestRecord.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UniInterestRecord.

        Created time  # noqa: E501

        :param create_time: The create_time of this UniInterestRecord.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

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
        if not isinstance(other, UniInterestRecord):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UniInterestRecord):
            return True

        return self.to_dict() != other.to_dict()
