#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    """
    Calculates the start and end indexes for pagination.
    Returns:
    return a tuple of size two containing a start and an end index
    """
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return start_idx, end_idx
