#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union


class Cache:
    """
        Wrapper class containing the init and store methods
        that initializes Redis with the arg data.
    """
    def __init__(self):
        """
            Initiate the instances of the class to connect to the
            Redis server and delete all the keys of the currently
            selected database using flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Create a random string using uuid, set it into the
            Redis server and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
