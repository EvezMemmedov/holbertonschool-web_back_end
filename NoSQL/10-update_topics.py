#!/usr/bin/env python3
"""
Module 10-update_topics
Contains a function that updates the topics of a school document.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the school name.

    Args:
        mongo_collection: pymongo collection object
        name (str): name of the school to update
        topics (list): list of topics taught in the school

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
