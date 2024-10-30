#!/usr/bin/python3
"""
LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    a class LRUCache that inherits from
    BaseCaching and is a caching system
    """

    def __init__(self):
        """Initialize the LRUCache"""
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        using the LRU algo to give the item value to the key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_used_key = self.key_order.pop(0)
                del self.cache_data[least_used_key]
                print(f"DISCARD: {least_used_key}")
            if key in self.key_order:
                self.key_order.remove(key)
            self.key_order.append(key)

    def get(self, key):
        """
        Returns the value associated with the key in the cache.
        """
        if key is not None and key in self.cache_data:
            self.key_order.remove(key)
            self.key_order.append(key)
            return self.cache_data[key]
        return None
