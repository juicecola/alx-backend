#!usr/bin/env python3
"""BaseCaching"""
from base_caching import BaseCaching
"""allowing us to use a double-ended queue data structure for efficient caching operations"""
from collections import deque

class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and implements the MRU caching system.
    """

    def __init__(self):
        """
        Initialize the MRUCache class.
        """
        super().__init__()
        # Initialize a deque to keep track of the order in which items are accessed (most recently used at the right end)
        self.usedKeys = deque()

    def put(self, key, item):
        """
        Add an item to the MRUCache.

        Args:
            key (str): The key of the item to be added.
            item (Any): The value of the item to be added.
        """
        if key is not None and item is not None:
            # Add the item to the cache
            self.cache_data[key] = item

            if key not in self.usedKeys:
                # If the key is not already in usedKeys, append it to the right end of the deque
                self.usedKeys.append(key)
            else:
                # If the key is already in usedKeys, move it to the right end (most recently used)
                self.usedKeys.remove(key)  # Remove the existing key from the deque
                self.usedKeys.append(key)  # Append the key to the right end of the deque

            if len(self.usedKeys) > self.MAX_ITEMS:
                # If the number of items in usedKeys exceeds the maximum capacity, evict the most recently used item
                mru_key = self.usedKeys.pop()  # Pop the rightmost (most recently used) key from the deque
                del self.cache_data[mru_key]  # Delete the corresponding entry from the cache
                print("DISCARD:", mru_key)

    def get(self, key):
        """
        Get an item from the MRUCache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The value of the item if it exists in the cache, otherwise None.
        """
        if key is not None and key in self.cache_data:
            # If the key is valid and exists in the cache, move it to the right end (most recently used)
            self.usedKeys.remove(key)  # Remove the existing key from the deque
            self.usedKeys.append(key)  # Append the key to the right end of the deque
            return self.cache_data[key]
        return None

