#!/usr/bin/env python3
"""Listing all documents of a mongo collection using Python"""


def list_all(mongo_collection):
    """
        A function that accepts a pymongo collection object as an
        argument and lists all the documents in the provided
        collections

        Args:
            @mongo_collection: The pymongo collection object
    """
    documents = []
    for doc in mongo_collection.find():
        documents.append(doc)
    return documents
