#!usr/bin/env python3
"""BaseCaching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """FIFO caching"""

    def __init__(self):
        """Initialiaze the FIFO cache"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """adds an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                """remove last item from queue and cache"""
                last_item = self.queue.pop(3)
                self.cache_data.pop(last_item)
                print("DISCARD:", last_item)

            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get an item by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
