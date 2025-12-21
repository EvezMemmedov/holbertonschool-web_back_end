#!/usr/bin/env python3
"""
Module 8-all
Contains a function that lists all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        A list of documents in the collection.
        Returns an empty list if the collection is empty.
    """
    return list(mongo_collection.find())
