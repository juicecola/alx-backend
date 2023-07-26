from base_caching import BaseCaching
from collections import defaultdict

class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and implements LFU caching algorithm.

    Attributes:
        cache_data (dict): A dictionary to store the key-value pairs as the cache data.
        frequency (defaultdict): A defaultdict to store the frequency count of each key.
        min_frequency (int): The minimum frequency count among all keys in the cache.

    Methods:
        update_frequency(key): Update the frequency count of a given key and update min_frequency accordingly.
        put(key, item): Add an item with the given key to the cache.
            If the cache exceeds its capacity, discard the least frequency used item(s) based on frequency count.
        get(key): Retrieve the value associated with the given key from the cache.
            If the key exists in the cache, update its frequency count and return the value. Otherwise, return None.
    """

    def __init__(self):
        """
        Initialize the LFUCache.
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.min_frequency = 0

    def update_frequency(self, key):
        """
        Update the frequency count of a given key and update min_frequency accordingly.

        Args:
            key (hashable): The key whose frequency count needs to be updated.
        """
        self.frequency[key] += 1
        if self.frequency[key] == 1:
            self.min_frequency = 1
        else:
            self.min_frequency = min(self.frequency.values())

    def put(self, key, item):
        """
        Add an item with the given key to the cache.

        If the cache exceeds its capacity, discard the least frequency used item(s) based on frequency count.

        Args:
            key (hashable): The key to be added to the cache.
            item: The value associated with the key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.update_frequency(key)

            if len(self.cache_data) > self.MAX_ITEMS:
                items_to_discard = [k for k in self.cache_data if self.frequency[k] == self.min_frequency]
                for k in items_to_discard:
                    del self.cache_data[k]
                    del self.frequency[k]

    def get(self, key):
        """
        Retrieve the value associated with the given key from the cache.

        If the key exists in the cache, update its frequency count and return the value. Otherwise, return None.

        Args:
            key (hashable): The key to retrieve the value.

        Returns:
            The value associated with the key if found, otherwise None.
        """
        if key is not None and key in self.cache_data:
            self.update_frequency(key)
            return self.cache_data[key]
        return None

