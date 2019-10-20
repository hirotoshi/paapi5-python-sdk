# coding: utf-8

"""
 Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

 Licensed under the Apache License, Version 2.0 (the "License").
 You may not use this file except in compliance with the License.
 A copy of the License is located at

     http://www.apache.org/licenses/LICENSE-2.0

 or in the "license" file accompanying this file. This file is distributed
 on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 express or implied. See the License for the specific language governing
 permissions and limitations under the License.
"""

"""
    ProductAdvertisingAPI

    https://webservices.amazon.com/paapi5/documentation/index.html  # noqa: E501
"""


import pprint
import re  # noqa: F401

import six

from paapi5_python_sdk.offer_availability import OfferAvailability  # noqa: F401,E501
from paapi5_python_sdk.offer_condition import OfferCondition  # noqa: F401,E501
from paapi5_python_sdk.offer_delivery_info import OfferDeliveryInfo  # noqa: F401,E501
from paapi5_python_sdk.offer_loyalty_points import OfferLoyaltyPoints  # noqa: F401,E501
from paapi5_python_sdk.offer_merchant_info import OfferMerchantInfo  # noqa: F401,E501
from paapi5_python_sdk.offer_price import OfferPrice  # noqa: F401,E501
from paapi5_python_sdk.offer_program_eligibility import OfferProgramEligibility  # noqa: F401,E501
from paapi5_python_sdk.offer_promotion import OfferPromotion  # noqa: F401,E501


class OfferListing(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'availability': 'OfferAvailability',
        'condition': 'OfferCondition',
        'delivery_info': 'OfferDeliveryInfo',
        'id': 'str',
        'is_buy_box_winner': 'bool',
        'loyalty_points': 'OfferLoyaltyPoints',
        'merchant_info': 'OfferMerchantInfo',
        'price': 'OfferPrice',
        'program_eligibility': 'OfferProgramEligibility',
        'promotions': 'list[OfferPromotion]',
        'saving_basis': 'OfferPrice',
        'violates_map': 'bool'
    }

    attribute_map = {
        'availability': 'Availability',
        'condition': 'Condition',
        'delivery_info': 'DeliveryInfo',
        'id': 'Id',
        'is_buy_box_winner': 'IsBuyBoxWinner',
        'loyalty_points': 'LoyaltyPoints',
        'merchant_info': 'MerchantInfo',
        'price': 'Price',
        'program_eligibility': 'ProgramEligibility',
        'promotions': 'Promotions',
        'saving_basis': 'SavingBasis',
        'violates_map': 'ViolatesMAP'
    }

    def __init__(self, availability=None, condition=None, delivery_info=None, id=None, is_buy_box_winner=None, loyalty_points=None, merchant_info=None, price=None, program_eligibility=None, promotions=None, saving_basis=None, violates_map=None):  # noqa: E501
        """OfferListing - a model defined in Swagger"""  # noqa: E501

        self._availability = None
        self._condition = None
        self._delivery_info = None
        self._id = None
        self._is_buy_box_winner = None
        self._loyalty_points = None
        self._merchant_info = None
        self._price = None
        self._program_eligibility = None
        self._promotions = None
        self._saving_basis = None
        self._violates_map = None
        self.discriminator = None

        if availability is not None:
            self.availability = availability
        if condition is not None:
            self.condition = condition
        if delivery_info is not None:
            self.delivery_info = delivery_info
        if id is not None:
            self.id = id
        if is_buy_box_winner is not None:
            self.is_buy_box_winner = is_buy_box_winner
        if loyalty_points is not None:
            self.loyalty_points = loyalty_points
        if merchant_info is not None:
            self.merchant_info = merchant_info
        if price is not None:
            self.price = price
        if program_eligibility is not None:
            self.program_eligibility = program_eligibility
        if promotions is not None:
            self.promotions = promotions
        if saving_basis is not None:
            self.saving_basis = saving_basis
        if violates_map is not None:
            self.violates_map = violates_map

    @property
    def availability(self):
        """Gets the availability of this OfferListing.  # noqa: E501


        :return: The availability of this OfferListing.  # noqa: E501
        :rtype: OfferAvailability
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this OfferListing.


        :param availability: The availability of this OfferListing.  # noqa: E501
        :type: OfferAvailability
        """

        self._availability = availability

    @property
    def condition(self):
        """Gets the condition of this OfferListing.  # noqa: E501


        :return: The condition of this OfferListing.  # noqa: E501
        :rtype: OfferCondition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this OfferListing.


        :param condition: The condition of this OfferListing.  # noqa: E501
        :type: OfferCondition
        """

        self._condition = condition

    @property
    def delivery_info(self):
        """Gets the delivery_info of this OfferListing.  # noqa: E501


        :return: The delivery_info of this OfferListing.  # noqa: E501
        :rtype: OfferDeliveryInfo
        """
        return self._delivery_info

    @delivery_info.setter
    def delivery_info(self, delivery_info):
        """Sets the delivery_info of this OfferListing.


        :param delivery_info: The delivery_info of this OfferListing.  # noqa: E501
        :type: OfferDeliveryInfo
        """

        self._delivery_info = delivery_info

    @property
    def id(self):
        """Gets the id of this OfferListing.  # noqa: E501


        :return: The id of this OfferListing.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OfferListing.


        :param id: The id of this OfferListing.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_buy_box_winner(self):
        """Gets the is_buy_box_winner of this OfferListing.  # noqa: E501


        :return: The is_buy_box_winner of this OfferListing.  # noqa: E501
        :rtype: bool
        """
        return self._is_buy_box_winner

    @is_buy_box_winner.setter
    def is_buy_box_winner(self, is_buy_box_winner):
        """Sets the is_buy_box_winner of this OfferListing.


        :param is_buy_box_winner: The is_buy_box_winner of this OfferListing.  # noqa: E501
        :type: bool
        """

        self._is_buy_box_winner = is_buy_box_winner

    @property
    def loyalty_points(self):
        """Gets the loyalty_points of this OfferListing.  # noqa: E501


        :return: The loyalty_points of this OfferListing.  # noqa: E501
        :rtype: OfferLoyaltyPoints
        """
        return self._loyalty_points

    @loyalty_points.setter
    def loyalty_points(self, loyalty_points):
        """Sets the loyalty_points of this OfferListing.


        :param loyalty_points: The loyalty_points of this OfferListing.  # noqa: E501
        :type: OfferLoyaltyPoints
        """

        self._loyalty_points = loyalty_points

    @property
    def merchant_info(self):
        """Gets the merchant_info of this OfferListing.  # noqa: E501


        :return: The merchant_info of this OfferListing.  # noqa: E501
        :rtype: OfferMerchantInfo
        """
        return self._merchant_info

    @merchant_info.setter
    def merchant_info(self, merchant_info):
        """Sets the merchant_info of this OfferListing.


        :param merchant_info: The merchant_info of this OfferListing.  # noqa: E501
        :type: OfferMerchantInfo
        """

        self._merchant_info = merchant_info

    @property
    def price(self):
        """Gets the price of this OfferListing.  # noqa: E501


        :return: The price of this OfferListing.  # noqa: E501
        :rtype: OfferPrice
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this OfferListing.


        :param price: The price of this OfferListing.  # noqa: E501
        :type: OfferPrice
        """

        self._price = price

    @property
    def program_eligibility(self):
        """Gets the program_eligibility of this OfferListing.  # noqa: E501


        :return: The program_eligibility of this OfferListing.  # noqa: E501
        :rtype: OfferProgramEligibility
        """
        return self._program_eligibility

    @program_eligibility.setter
    def program_eligibility(self, program_eligibility):
        """Sets the program_eligibility of this OfferListing.


        :param program_eligibility: The program_eligibility of this OfferListing.  # noqa: E501
        :type: OfferProgramEligibility
        """

        self._program_eligibility = program_eligibility

    @property
    def promotions(self):
        """Gets the promotions of this OfferListing.  # noqa: E501


        :return: The promotions of this OfferListing.  # noqa: E501
        :rtype: list[OfferPromotion]
        """
        return self._promotions

    @promotions.setter
    def promotions(self, promotions):
        """Sets the promotions of this OfferListing.


        :param promotions: The promotions of this OfferListing.  # noqa: E501
        :type: list[OfferPromotion]
        """

        self._promotions = promotions

    @property
    def saving_basis(self):
        """Gets the saving_basis of this OfferListing.  # noqa: E501


        :return: The saving_basis of this OfferListing.  # noqa: E501
        :rtype: OfferPrice
        """
        return self._saving_basis

    @saving_basis.setter
    def saving_basis(self, saving_basis):
        """Sets the saving_basis of this OfferListing.


        :param saving_basis: The saving_basis of this OfferListing.  # noqa: E501
        :type: OfferPrice
        """

        self._saving_basis = saving_basis

    @property
    def violates_map(self):
        """Gets the violates_map of this OfferListing.  # noqa: E501


        :return: The violates_map of this OfferListing.  # noqa: E501
        :rtype: bool
        """
        return self._violates_map

    @violates_map.setter
    def violates_map(self, violates_map):
        """Sets the violates_map of this OfferListing.


        :param violates_map: The violates_map of this OfferListing.  # noqa: E501
        :type: bool
        """

        self._violates_map = violates_map

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(OfferListing, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OfferListing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
