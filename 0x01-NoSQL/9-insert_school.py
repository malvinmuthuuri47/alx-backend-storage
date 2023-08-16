#!/usr/bin/env python3
"""
    A module that implements the functionality of adding a document
    in a MongoDb collection
"""


def insert_school(mongo_collection, **kwargs):
    """
        This function adds new documents passed in as keyword args
        into the mongo_collection

        Args:
            @mongo_collection: The MongoDb collection
            kwargs: The new document(s) to be inserted into the collection
    """
    inserted_doc = mongo_collection.insert_one(kwargs)
    return inserted_doc.inserted_id
