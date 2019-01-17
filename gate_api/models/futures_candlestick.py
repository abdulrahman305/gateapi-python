# coding: utf-8

"""
    Gate API v4

    APIv4 futures provides all sorts of futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    OpenAPI spec version: 1.2.0
    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FuturesCandlestick(object):
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
        't': 'float',
        'v': 'int',
        'c': 'str',
        'h': 'str',
        'l': 'str',
        'o': 'str'
    }

    attribute_map = {
        't': 't',
        'v': 'v',
        'c': 'c',
        'h': 'h',
        'l': 'l',
        'o': 'o'
    }

    def __init__(self, t=None, v=None, c=None, h=None, l=None, o=None):  # noqa: E501
        """FuturesCandlestick - a model defined in OpenAPI"""  # noqa: E501

        self._t = None
        self._v = None
        self._c = None
        self._h = None
        self._l = None
        self._o = None
        self.discriminator = None

        if t is not None:
            self.t = t
        if v is not None:
            self.v = v
        if c is not None:
            self.c = c
        if h is not None:
            self.h = h
        if l is not None:
            self.l = l
        if o is not None:
            self.o = o

    @property
    def t(self):
        """Gets the t of this FuturesCandlestick.  # noqa: E501

        Unix timestamp in seconds  # noqa: E501

        :return: The t of this FuturesCandlestick.  # noqa: E501
        :rtype: float
        """
        return self._t

    @t.setter
    def t(self, t):
        """Sets the t of this FuturesCandlestick.

        Unix timestamp in seconds  # noqa: E501

        :param t: The t of this FuturesCandlestick.  # noqa: E501
        :type: float
        """

        self._t = t

    @property
    def v(self):
        """Gets the v of this FuturesCandlestick.  # noqa: E501

        size volume. Only returned if `contract` is not prefixed  # noqa: E501

        :return: The v of this FuturesCandlestick.  # noqa: E501
        :rtype: int
        """
        return self._v

    @v.setter
    def v(self, v):
        """Sets the v of this FuturesCandlestick.

        size volume. Only returned if `contract` is not prefixed  # noqa: E501

        :param v: The v of this FuturesCandlestick.  # noqa: E501
        :type: int
        """

        self._v = v

    @property
    def c(self):
        """Gets the c of this FuturesCandlestick.  # noqa: E501

        Close price  # noqa: E501

        :return: The c of this FuturesCandlestick.  # noqa: E501
        :rtype: str
        """
        return self._c

    @c.setter
    def c(self, c):
        """Sets the c of this FuturesCandlestick.

        Close price  # noqa: E501

        :param c: The c of this FuturesCandlestick.  # noqa: E501
        :type: str
        """

        self._c = c

    @property
    def h(self):
        """Gets the h of this FuturesCandlestick.  # noqa: E501

        Highest price  # noqa: E501

        :return: The h of this FuturesCandlestick.  # noqa: E501
        :rtype: str
        """
        return self._h

    @h.setter
    def h(self, h):
        """Sets the h of this FuturesCandlestick.

        Highest price  # noqa: E501

        :param h: The h of this FuturesCandlestick.  # noqa: E501
        :type: str
        """

        self._h = h

    @property
    def l(self):
        """Gets the l of this FuturesCandlestick.  # noqa: E501

        Lowest price  # noqa: E501

        :return: The l of this FuturesCandlestick.  # noqa: E501
        :rtype: str
        """
        return self._l

    @l.setter
    def l(self, l):
        """Sets the l of this FuturesCandlestick.

        Lowest price  # noqa: E501

        :param l: The l of this FuturesCandlestick.  # noqa: E501
        :type: str
        """

        self._l = l

    @property
    def o(self):
        """Gets the o of this FuturesCandlestick.  # noqa: E501

        Open price  # noqa: E501

        :return: The o of this FuturesCandlestick.  # noqa: E501
        :rtype: str
        """
        return self._o

    @o.setter
    def o(self, o):
        """Sets the o of this FuturesCandlestick.

        Open price  # noqa: E501

        :param o: The o of this FuturesCandlestick.  # noqa: E501
        :type: str
        """

        self._o = o

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
        if not isinstance(other, FuturesCandlestick):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
