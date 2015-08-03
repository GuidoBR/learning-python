"""
Problem:
Application needs one, and only one, instance of an object. Additionally, lazy
initialization and global access are necessary.

Structure:
Make the class of the single instance responsible for access and
"initialization on first use". The single instance is a private static
attribute. The accessor function is a public static method.

"Singleton pattern was once considered to be a design pattern but now is
considered to be an Anti-pattern due to the shared state it introduces, similar
to using global variables. - Django Design Patterns and Best Pratices"
"""


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
