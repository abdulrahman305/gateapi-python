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


class FuturesPriceTriggeredOrder(object):
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
        'initial': 'FuturesInitialOrder',
        'trigger': 'FuturesPriceTrigger',
        'id': 'int',
        'user': 'int',
        'create_time': 'float',
        'finish_time': 'float',
        'trade_id': 'int',
        'status': 'str',
        'finish_as': 'str',
        'reason': 'str',
        'order_type': 'str',
        'me_order_id': 'int'
    }

    attribute_map = {
        'initial': 'initial',
        'trigger': 'trigger',
        'id': 'id',
        'user': 'user',
        'create_time': 'create_time',
        'finish_time': 'finish_time',
        'trade_id': 'trade_id',
        'status': 'status',
        'finish_as': 'finish_as',
        'reason': 'reason',
        'order_type': 'order_type',
        'me_order_id': 'me_order_id'
    }

    def __init__(self, initial=None, trigger=None, id=None, user=None, create_time=None, finish_time=None, trade_id=None, status=None, finish_as=None, reason=None, order_type=None, me_order_id=None, local_vars_configuration=None):  # noqa: E501
        # type: (FuturesInitialOrder, FuturesPriceTrigger, int, int, float, float, int, str, str, str, str, int, Configuration) -> None
        """FuturesPriceTriggeredOrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._initial = None
        self._trigger = None
        self._id = None
        self._user = None
        self._create_time = None
        self._finish_time = None
        self._trade_id = None
        self._status = None
        self._finish_as = None
        self._reason = None
        self._order_type = None
        self._me_order_id = None
        self.discriminator = None

        self.initial = initial
        self.trigger = trigger
        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if trade_id is not None:
            self.trade_id = trade_id
        if status is not None:
            self.status = status
        if finish_as is not None:
            self.finish_as = finish_as
        if reason is not None:
            self.reason = reason
        if order_type is not None:
            self.order_type = order_type
        if me_order_id is not None:
            self.me_order_id = me_order_id

    @property
    def initial(self):
        """Gets the initial of this FuturesPriceTriggeredOrder.  # noqa: E501


        :return: The initial of this FuturesPriceTriggeredOrder.  # noqa: E501
        :rtype: FuturesInitialOrder
        """
        return self._initial

    @initial.setter
    def initial(self, initial):
        """Sets the initial of this FuturesPriceTriggeredOrder.


        :param initial: The initial of this FuturesPriceTriggeredOrder.  # noqa: E501
        :type: FuturesInitialOrder
        """
        if self.local_vars_configuration.client_side_validation and initial is None:  # noqa: E501
            raise ValueError("Invalid value for `initial`, must not be `None`")  # noqa: E501

        self._initial = initial

    @property
    def trigger(self):
        """Gets the trigger of this FuturesPriceTriggeredOrder.  # noqa: E501


        :return: The trigger of this FuturesPriceTriggeredOrder.  # noqa: E501
        :rtype: FuturesPriceTrigger
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this FuturesPriceTriggeredOrder.


        :param trigger: The trigger of this FuturesPriceTriggeredOrder.  # noqa: E501
        :type: FuturesPriceTrigger
        """
        if self.local_vars_configuration.client_side_validation and trigger is None:  # noqa: E501
            raise ValueError("Invalid value for `trigger`, must not be `None`")  # noqa: E501

        self._trigger = trigger

    @property
    def id(self):
        """Gets the id of this FuturesPriceTriggeredOrder.  # noqa: E501

        Auto order ID  # noqa: E501

        :return: The id of this FuturesPriceTriggeredOrder.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FuturesPriceTriggeredOrder.

        Auto order ID  # noqa: E501

        :param id: The id of this FuturesPriceTriggeredOrder.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user(self):
        """Gets the user of this FuturesPriceTriggeredOrder.  # noqa: E501

        User ID  # noqa: E501

        :return: The user of this FuturesPriceTriggeredOrder.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this FuturesPriceTriggeredOrder.

        User ID  # noqa: E501

        :param user: The user of this FuturesPriceTriggeredOrder.  # noqa: E501
        :type: int
        """

        self._user = user

    @property
    def create_time(self):
        """Gets the create_time of this FuturesPriceTriggeredOrder.  # noqa: E501

        Creation time  # noqa: E501

        :return: The create_time of this FuturesPriceTriggeredOrder.  # noqa: E501
        :rtype: float
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this FuturesPriceTriggeredOrder.

        Creation time  # noqa: E501

        :param create_time: The create_time of this FuturesPriceTriggeredOrder.  # noqa: E501
        :type: float
        """

        self._create_time = create_time

    @property
    def finish_time(self):
        """Gets the finish_time of this FuturesPriceTriggeredOrder.  # noqa: E501

        Finished time  # noqa: E501

        :return: The finish_time of this FuturesPriceTriggeredOrder.  # noqa: E501
        :rtype: float
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this FuturesPriceTriggeredOrder.

        Finished time  # noqa: E501

        :param finish_time: The finish_time of this FuturesPriceTriggeredOrder.  # noqa: E501
        :type: float
        """

        self._finish_time = finish_time

    @property
    def trade_id(self):
        """Gets the trade_id of this FuturesPriceTriggeredOrder.  # noqa: E501

        ID of the newly created order on condition triggered  # noqa: E501

        :return: The trade_id of this FuturesPriceTriggeredOrder.  # noqa: E501
        :rtype: int
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """Sets the trade_id of this FuturesPriceTriggeredOrder.

        ID of the newly created order on condition triggered  # noqa: E501

        :param trade_id: The trade_id of this FuturesPriceTriggeredOrder.  # noqa: E501
        :type: int
        """

        self._trade_id = trade_id

    @property
    def status(self):
        """Gets the status of this FuturesPriceTriggeredOrder.  # noqa: E501

        Auto order status  - `open`: order is active - `finished`: order is finished - `inactive`: order is not active, only for close-long-order or close-short-order - `invalid`: order is invalid, only for close-long-order or close-short-order  # noqa: E501

        :return: The status of this FuturesPriceTriggeredOrder.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FuturesPriceTriggeredOrder.

        Auto order status  - `open`: order is active - `finished`: order is finished - `inactive`: order is not active, only for close-long-order or close-short-order - `invalid`: order is invalid, only for close-long-order or close-short-order  # noqa: E501

        :param status: The status of this FuturesPriceTriggeredOrder.  # noqa: E501
        :type: str
        """
        allowed_values = ["open", "finished", "inactive", "invalid"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def finish_as(self):
        """Gets the finish_as of this FuturesPriceTriggeredOrder.  # noqa: E501

        How order is finished  # noqa: E501

        :return: The finish_as of this FuturesPriceTriggeredOrder.  # noqa: E501
        :rtype: str
        """
        return self._finish_as

    @finish_as.setter
    def finish_as(self, finish_as):
        """Sets the finish_as of this FuturesPriceTriggeredOrder.

        How order is finished  # noqa: E501

        :param finish_as: The finish_as of this FuturesPriceTriggeredOrder.  # noqa: E501
        :type: str
        """
        allowed_values = ["cancelled", "succeeded", "failed", "expired"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and finish_as not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `finish_as` ({0}), must be one of {1}"  # noqa: E501
                .format(finish_as, allowed_values)
            )

        self._finish_as = finish_as

    @property
    def reason(self):
        """Gets the reason of this FuturesPriceTriggeredOrder.  # noqa: E501

        Additional remarks on how the order was finished  # noqa: E501

        :return: The reason of this FuturesPriceTriggeredOrder.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this FuturesPriceTriggeredOrder.

        Additional remarks on how the order was finished  # noqa: E501

        :param reason: The reason of this FuturesPriceTriggeredOrder.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def order_type(self):
        """Gets the order_type of this FuturesPriceTriggeredOrder.  # noqa: E501

        Take-profit/stop-loss types, which include:  - `close-long-order`: order take-profit/stop-loss, close long position - `close-short-order`: order take-profit/stop-loss, close short position - `close-long-position`: position take-profit/stop-loss, close long position - `close-short-position`: position take-profit/stop-loss, close short position - `plan-close-long-position`: position planned take-profit/stop-loss, close long position - `plan-close-short-position`: position planned take-profit/stop-loss, close short position  The order take-profit/stop-loss can not be passed by request. These two types are read only.  # noqa: E501

        :return: The order_type of this FuturesPriceTriggeredOrder.  # noqa: E501
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this FuturesPriceTriggeredOrder.

        Take-profit/stop-loss types, which include:  - `close-long-order`: order take-profit/stop-loss, close long position - `close-short-order`: order take-profit/stop-loss, close short position - `close-long-position`: position take-profit/stop-loss, close long position - `close-short-position`: position take-profit/stop-loss, close short position - `plan-close-long-position`: position planned take-profit/stop-loss, close long position - `plan-close-short-position`: position planned take-profit/stop-loss, close short position  The order take-profit/stop-loss can not be passed by request. These two types are read only.  # noqa: E501

        :param order_type: The order_type of this FuturesPriceTriggeredOrder.  # noqa: E501
        :type: str
        """

        self._order_type = order_type

    @property
    def me_order_id(self):
        """Gets the me_order_id of this FuturesPriceTriggeredOrder.  # noqa: E501

        Corresponding order ID of order take-profit/stop-loss.  # noqa: E501

        :return: The me_order_id of this FuturesPriceTriggeredOrder.  # noqa: E501
        :rtype: int
        """
        return self._me_order_id

    @me_order_id.setter
    def me_order_id(self, me_order_id):
        """Sets the me_order_id of this FuturesPriceTriggeredOrder.

        Corresponding order ID of order take-profit/stop-loss.  # noqa: E501

        :param me_order_id: The me_order_id of this FuturesPriceTriggeredOrder.  # noqa: E501
        :type: int
        """

        self._me_order_id = me_order_id

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
        if not isinstance(other, FuturesPriceTriggeredOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FuturesPriceTriggeredOrder):
            return True

        return self.to_dict() != other.to_dict()
