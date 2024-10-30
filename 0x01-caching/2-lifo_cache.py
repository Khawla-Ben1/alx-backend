#!/usr/bin/python3
"""
LIFO Caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    a class LIFOCache that inherits from
    BaseCaching and is a caching system
    """

    def __init__(self):
        """Initialize the LIFOCache"""
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """
        using the LIFO algo to assign the item value to the key
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.key_indexes.remove(key)
                else:
                    last_item = self.key_indexes.pop()
                    # Remove the last item - LIFO
                    del self.cache_data[last_item]
                    print("DISCARD:", last_item)
            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """
        Returns the value associated with the key in the cache.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
