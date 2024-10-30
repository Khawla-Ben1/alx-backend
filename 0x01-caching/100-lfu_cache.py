#!/usr/bin/python3
"""
LFU Caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    a class LFUCache that inherits from
    BaseCaching and is a caching system.
    """

    def __init__(self):
        """
        Initialize the LFUCache.
        """
        super().__init__()
        self.item_freqs = {}

    def put(self, key, item):
        """using LFU algo to gives the item value to the key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            item_to_discard = min(self.item_freqs, key=self.item_freqs.get)
            self.item_freqs.pop(item_to_discard)
            self.cache_data.pop(item_to_discard)
            print(f"DISCARD: {item_to_discard}")
        if key not in self.item_freqs:
            self.item_freqs[key] = 0
        else:
            self.item_freqs[key] += 1

    def get(self, key):
        """Returns the value associated with the key in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        self.item_freqs[key] += 1
        return self.cache_data.get(key)
