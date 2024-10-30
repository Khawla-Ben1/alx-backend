#!/usr/bin/python3
"""
MRU Caching
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    a class MRUCache that inherits from
    BaseCaching and is a caching system
    """

    def __init__(self):
        """Initialize the MRUCache."""
        super().__init__()
        self.most_ru_order = OrderedDict()

    def put(self, key, item):
        """
        using the MRU algo to gives the item value to the key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.most_ru_order[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            most_recently_item = next(iter(self.most_ru_order))
            del self.cache_data[most_recently_item]
            print(f"DISCARD: {most_recently_item}")
        if len(self.most_ru_order) > BaseCaching.MAX_ITEMS:
            self.most_ru_order.popitem(last=False)
        self.most_ru_order.move_to_end(key, last=False)

    def get(self, key):
        """
        Returns the value associated with the key in the cache.
        """
        if key is not None and key in self.cache_data:
            self.most_ru_order.move_to_end(key, last=False)
            return self.cache_data[key]
        return None
