#!/usr/bin/env python3
"""A module that changes school topics"""


def update_topics(mongo_collection, name, topics):
    """
        Function that changes all topics of a school
        document based on name

        Args:
            mongo_collection: The document collection
            name: The name of the school
            Topics: The topics to update
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )
