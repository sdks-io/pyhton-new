# -*- coding: utf-8 -*-

"""
swaggerpetstore

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from swaggerpetstore.api_helper import APIHelper


class Order(object):

    """Implementation of the 'Order' model.

    TODO: type model description here.

    Attributes:
        id (long|int): TODO: type description here.
        pet_id (long|int): TODO: type description here.
        quantity (int): TODO: type description here.
        ship_date (datetime): TODO: type description here.
        status (Status1Enum): Order Status
        complete (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "pet_id": 'petId',
        "quantity": 'quantity',
        "ship_date": 'shipDate',
        "status": 'status',
        "complete": 'complete'
    }

    _optionals = [
        'id',
        'pet_id',
        'quantity',
        'ship_date',
        'status',
        'complete',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 pet_id=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 ship_date=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 complete=APIHelper.SKIP):
        """Constructor for the Order class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if pet_id is not APIHelper.SKIP:
            self.pet_id = pet_id 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if ship_date is not APIHelper.SKIP:
            self.ship_date = APIHelper.apply_datetime_converter(ship_date, APIHelper.RFC3339DateTime) if ship_date else None 
        if status is not APIHelper.SKIP:
            self.status = status 
        if complete is not APIHelper.SKIP:
            self.complete = complete 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        pet_id = dictionary.get("petId") if dictionary.get("petId") else APIHelper.SKIP
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else APIHelper.SKIP
        ship_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("shipDate")).datetime if dictionary.get("shipDate") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        complete = dictionary.get("complete") if "complete" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   pet_id,
                   quantity,
                   ship_date,
                   status,
                   complete)
