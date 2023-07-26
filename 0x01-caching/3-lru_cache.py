#!usr/bin/env python3
"""BaseCaching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching and implements the LRU caching system.
    """

    def __init__(self):
        """
        Initialize the LRUCache class.
        """
        super().__init__()
        # Initialize a list to keep track of the order in which items are accessed
        self.usedKeys = []

    def put(self, key, item):
        """
        Add an item to the LRUCache.

        Args:
            key (str): The key of the item to be added.
            item (Any): The value of the item to be added.
        """
        if key is not None and item is not None:
            # Add the item to the cache
            self.cache_data[key] = item

            if key not in self.usedKeys:
                # If the key is not already in usedKeys, append it to the list
                self.usedKeys.append(key)
            else:
                # If the key is already in usedKeys, move it to the end (most recently used)
                self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))

            if len(self.usedKeys) > self.MAX_ITEMS:
                # If the number of items in usedKeys exceeds the maximum capacity, evict the least recently used item
                lru_key = self.usedKeys.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)

    def get(self, key):
        """
        Get an item from the LRUCache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The value of the item if it exists in the cache, otherwise None.
        """
        if key is not None and key in self.cache_data:
            # If the key is valid and exists in the cache, move it to the end (most recently used)
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data[key]
        return None

