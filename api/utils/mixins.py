from pymongo.collection import Collection

from api import get_nosql


class NoSQLBaseMixin:
    collection: Collection

    def __init__(self, *args, **kwargs):
        self.collection = get_nosql()[self.__class__.__name__.lower()]
        for dictionary in args:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])
