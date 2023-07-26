#!usr/bin/env python3
"""BaseCaching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU cache"""

    def __init__(self):
        """Initialiaze the LRU cache"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """adds an item in the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                """remove least used item from queue and cache"""
                lru_item = self.queue.pop(0)
                self.cache_data.pop(lru_item)
                print("DISCARD:", lru_item)

            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get an item by key"""
        if key is not None and key in self.cache_data:
            """move accssed item to end of queue"""
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
