#!/usr/bin/env python3
"""
Docstring for pagination.0-simple_helper_function
"""


def index_range(page, page_size):
    """
    Docstring for index_range
    :param page: Description
    :param page_size: Description
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
