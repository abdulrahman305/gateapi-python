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


class UidPushOrder(object):
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
        'id': 'int',
        'push_uid': 'int',
        'receive_uid': 'int',
        'currency': 'str',
        'amount': 'str',
        'create_time': 'int',
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'push_uid': 'push_uid',
        'receive_uid': 'receive_uid',
        'currency': 'currency',
        'amount': 'amount',
        'create_time': 'create_time',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, id=None, push_uid=None, receive_uid=None, currency=None, amount=None, create_time=None, status=None, message=None, local_vars_configuration=None):  # noqa: E501
        # type: (int, int, int, str, str, int, str, str, Configuration) -> None
        """UidPushOrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._push_uid = None
        self._receive_uid = None
        self._currency = None
        self._amount = None
        self._create_time = None
        self._status = None
        self._message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if push_uid is not None:
            self.push_uid = push_uid
        if receive_uid is not None:
            self.receive_uid = receive_uid
        if currency is not None:
            self.currency = currency
        if amount is not None:
            self.amount = amount
        if create_time is not None:
            self.create_time = create_time
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message

    @property
    def id(self):
        """Gets the id of this UidPushOrder.  # noqa: E501

        Order ID  # noqa: E501

        :return: The id of this UidPushOrder.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UidPushOrder.

        Order ID  # noqa: E501

        :param id: The id of this UidPushOrder.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def push_uid(self):
        """Gets the push_uid of this UidPushOrder.  # noqa: E501

        Initiator User ID  # noqa: E501

        :return: The push_uid of this UidPushOrder.  # noqa: E501
        :rtype: int
        """
        return self._push_uid

    @push_uid.setter
    def push_uid(self, push_uid):
        """Sets the push_uid of this UidPushOrder.

        Initiator User ID  # noqa: E501

        :param push_uid: The push_uid of this UidPushOrder.  # noqa: E501
        :type: int
        """

        self._push_uid = push_uid

    @property
    def receive_uid(self):
        """Gets the receive_uid of this UidPushOrder.  # noqa: E501

        Recipient User ID  # noqa: E501

        :return: The receive_uid of this UidPushOrder.  # noqa: E501
        :rtype: int
        """
        return self._receive_uid

    @receive_uid.setter
    def receive_uid(self, receive_uid):
        """Sets the receive_uid of this UidPushOrder.

        Recipient User ID  # noqa: E501

        :param receive_uid: The receive_uid of this UidPushOrder.  # noqa: E501
        :type: int
        """

        self._receive_uid = receive_uid

    @property
    def currency(self):
        """Gets the currency of this UidPushOrder.  # noqa: E501

        Currency name  # noqa: E501

        :return: The currency of this UidPushOrder.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this UidPushOrder.

        Currency name  # noqa: E501

        :param currency: The currency of this UidPushOrder.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this UidPushOrder.  # noqa: E501

        Transfer amount  # noqa: E501

        :return: The amount of this UidPushOrder.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this UidPushOrder.

        Transfer amount  # noqa: E501

        :param amount: The amount of this UidPushOrder.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def create_time(self):
        """Gets the create_time of this UidPushOrder.  # noqa: E501

        Creation time  # noqa: E501

        :return: The create_time of this UidPushOrder.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UidPushOrder.

        Creation time  # noqa: E501

        :param create_time: The create_time of this UidPushOrder.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def status(self):
        """Gets the status of this UidPushOrder.  # noqa: E501

        Withdrawal Status  - CREATING: Creating - PENDING: Waiting for receiving(Please contact the other party to accept the transfer on the Gate official website) - CANCELLING: Cancelling - CANCELLED: Revoked - REFUSING: Rejection - REFUSED: Rejected - RECEIVING: Receiving - RECEIVED: Success  # noqa: E501

        :return: The status of this UidPushOrder.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UidPushOrder.

        Withdrawal Status  - CREATING: Creating - PENDING: Waiting for receiving(Please contact the other party to accept the transfer on the Gate official website) - CANCELLING: Cancelling - CANCELLED: Revoked - REFUSING: Rejection - REFUSED: Rejected - RECEIVING: Receiving - RECEIVED: Success  # noqa: E501

        :param status: The status of this UidPushOrder.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def message(self):
        """Gets the message of this UidPushOrder.  # noqa: E501

        PENDING Reason Tips  # noqa: E501

        :return: The message of this UidPushOrder.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this UidPushOrder.

        PENDING Reason Tips  # noqa: E501

        :param message: The message of this UidPushOrder.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, UidPushOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UidPushOrder):
            return True

        return self.to_dict() != other.to_dict()
