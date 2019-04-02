# coding: utf-8

"""
    Gate API v4

    APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    OpenAPI spec version: 4.6.1
    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Trade(object):
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
        'id': 'str',
        'create_time': 'str',
        'side': 'str',
        'amount': 'str',
        'price': 'str',
        'order_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'side': 'side',
        'amount': 'amount',
        'price': 'price',
        'order_id': 'order_id'
    }

    def __init__(self, id=None, create_time=None, side=None, amount=None, price=None, order_id=None):  # noqa: E501
        """Trade - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._create_time = None
        self._side = None
        self._amount = None
        self._price = None
        self._order_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if side is not None:
            self.side = side
        if amount is not None:
            self.amount = amount
        if price is not None:
            self.price = price
        if order_id is not None:
            self.order_id = order_id

    @property
    def id(self):
        """Gets the id of this Trade.  # noqa: E501

        Trade ID  # noqa: E501

        :return: The id of this Trade.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Trade.

        Trade ID  # noqa: E501

        :param id: The id of this Trade.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this Trade.  # noqa: E501

        Trading time  # noqa: E501

        :return: The create_time of this Trade.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Trade.

        Trading time  # noqa: E501

        :param create_time: The create_time of this Trade.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def side(self):
        """Gets the side of this Trade.  # noqa: E501

        Order side  # noqa: E501

        :return: The side of this Trade.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this Trade.

        Order side  # noqa: E501

        :param side: The side of this Trade.  # noqa: E501
        :type: str
        """
        allowed_values = ["buy", "sell"]  # noqa: E501
        if side not in allowed_values:
            raise ValueError(
                "Invalid value for `side` ({0}), must be one of {1}"  # noqa: E501
                .format(side, allowed_values)
            )

        self._side = side

    @property
    def amount(self):
        """Gets the amount of this Trade.  # noqa: E501

        Trade amount  # noqa: E501

        :return: The amount of this Trade.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Trade.

        Trade amount  # noqa: E501

        :param amount: The amount of this Trade.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def price(self):
        """Gets the price of this Trade.  # noqa: E501

        Order price  # noqa: E501

        :return: The price of this Trade.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Trade.

        Order price  # noqa: E501

        :param price: The price of this Trade.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def order_id(self):
        """Gets the order_id of this Trade.  # noqa: E501

        Related order ID. No value in public endpoints  # noqa: E501

        :return: The order_id of this Trade.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Trade.

        Related order ID. No value in public endpoints  # noqa: E501

        :param order_id: The order_id of this Trade.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

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
        if not isinstance(other, Trade):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
