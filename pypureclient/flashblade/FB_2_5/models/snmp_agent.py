# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.5, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_5 import models

class SnmpAgent(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'engine_id': 'str',
        'version': 'str',
        'v2c': 'SnmpV2c',
        'v3': 'SnmpV3'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'engine_id': 'engine_id',
        'version': 'version',
        'v2c': 'v2c',
        'v3': 'v3'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        engine_id=None,  # type: str
        version=None,  # type: str
        v2c=None,  # type: models.SnmpV2c
        v3=None,  # type: models.SnmpV3
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            engine_id (str): An SNMP agent's adminstration domain unique name.
            version (str): Version of the SNMP protocol to be used by an SNMP manager in communications with Purity's SNMP agent. Valid values are `v2c` and `v3`.
            v2c (SnmpV2c)
            v3 (SnmpV3)
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if engine_id is not None:
            self.engine_id = engine_id
        if version is not None:
            self.version = version
        if v2c is not None:
            self.v2c = v2c
        if v3 is not None:
            self.v3 = v3

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SnmpAgent`".format(key))
        if key == "engine_id" and value is not None:
            if len(value) > 32:
                raise ValueError("Invalid value for `engine_id`, length must be less than or equal to `32`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            return None
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
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
        if issubclass(SnmpAgent, dict):
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
        if not isinstance(other, SnmpAgent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
