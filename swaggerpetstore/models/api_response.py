# -*- coding: utf-8 -*-

"""
swaggerpetstore

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerpetstore.api_helper import APIHelper


class ApiResponse(object):

    """Implementation of the 'ApiResponse' model.

    TODO: type model description here.

    Attributes:
        code (int): TODO: type description here.
        mtype (str): TODO: type description here.
        message (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code',
        "mtype": 'type',
        "message": 'message'
    }

    _optionals = [
        'code',
        'mtype',
        'message',
    ]

    def __init__(self,
                 code=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 message=APIHelper.SKIP):
        """Constructor for the ApiResponse class"""

        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if message is not APIHelper.SKIP:
            self.message = message 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        # Return an object of this model
        return cls(code,
                   mtype,
                   message)
