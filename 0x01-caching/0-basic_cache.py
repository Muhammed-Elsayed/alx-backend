#!/usr/bin/python3
from base_caching import BaseCaching
""" BasicCache module
"""


class BasicCache(BaseCaching):
    """ BaseCache defines:
      -
    """
    """funct to append to the cache"""
    def put(self, key, item):
        if key is None or item is None:
            pass

        self.cache_data[key] = item

    "funct to get a the value by the key"
    def get(self, key):
        if key is None or self.cache_data[key] is None:
            return(None)
        return(self.cache_data[key])
