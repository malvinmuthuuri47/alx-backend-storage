#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """A method that takes a Callable and returns a Callable"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
            This method implements the functionality of storing the
            number of times the store method has been called.

            It ensures the key is a qualified name by using the
            __qualname__ dunder method and increases the value of
            the key by using the incr() method
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


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

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Create a random string using uuid, set it into the
            Redis server and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """
            A function that gets the value stored in the data key, calls
            the appropriate callable on the data and returns the
            data.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
            This is the first callable that decodes the data from bytes
            to a python string using the utf-8 decode
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
            This is the second callable that converts the key to an
            int
        """
        return self.get(key, fn=int)

    def count_calls(method: Callable) -> Callable:
        """A method that takes a Callable and returns a Callable"""
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """
                This method implements the functionality of storing the
                number of times the store method has been called.

                It ensures the key is a qualified name by using the
                __qualname__ dunder method and increases the value of
                the key by using the incr() method
            """
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper
