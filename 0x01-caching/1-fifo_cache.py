#!/usr/bin/python3
"""
FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    a class FIFOCache that inherits from
    BaseCaching and is a caching system
    """

    def __init__(self):
        """Initializes the FIFOCache"""
        super().__init__()

    def put(self, key, item):
        """
        using the fifo algo to give the item value to the key
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

            self.cache_data[key] = item

    def get(self, key):
        """
        Returns:
            The value associated with the key or None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
