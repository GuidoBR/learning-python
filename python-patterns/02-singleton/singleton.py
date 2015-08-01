"""
Problem:
Application needs one, and only one, instance of an object. Additionally, lazy
initialization and global access are necessary.

Structure:
Make the class of the single instance responsible for access and
"initialization on first use". The single instance is a private static
attribute. The accessor function is a public static method.
"""


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
