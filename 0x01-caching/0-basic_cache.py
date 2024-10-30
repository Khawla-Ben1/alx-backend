#!/usr/bin/env python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    a class BasicCache that inherits
    from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """Assigns the item value to the key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value associated with the key.
        Returns:
            The value associated with the key, or
            None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
