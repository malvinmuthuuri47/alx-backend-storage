#!/usr/bin/env python3
"""A module that returns a list of schools having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
        A function that returns a list of Schools having a specific
        topic

        Args:
            @mongo_collection: The pymongo collection object
            @topic: The topic to search for
    """
    return list(mongo_collection.find({"topics": topic}))
