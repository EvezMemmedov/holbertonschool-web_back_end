#!/usr/bin/env python3
"""
Module 11-schools_by_topic
Contains a function that returns a list of schools having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of school documents that have a specific topic.

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for

    Returns:
        List of documents that contain the topic.
        Returns an empty list if no school has the topic.
    """
    return list(mongo_collection.find({"topics": topic}))
