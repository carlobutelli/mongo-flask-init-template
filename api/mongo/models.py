#!/usr/bin/env python3
from api import get_nosql
from api.utils.mixins import NoSQLBaseMixin


class ListingsAndReviews(NoSQLBaseMixin):
    __collection__ = 'listingsAndReviews'

    @classmethod
    def deserializer(cls) -> list:
        data = []
        collection = get_nosql()[cls.__collection__]

        return data


class Test(NoSQLBaseMixin):
    __collection__ = 'test'

    name: str = None
    type: str = None

    @classmethod
    def deserializer(cls) -> object:
        collection = get_nosql()[cls.__collection__]

        document = {
            "name": "Carlo",
            "type": "Test"
        }

        inserted_id = collection.insert_one(document).inserted_id
        # print(f"Inserted id: {inserted_id}")
        return inserted_id


class Person(NoSQLBaseMixin):
    __collection__ = 'person'

    guid: str = None
    first_name: str = None
    last_name: str = None
    age: int = None

    @classmethod
    def deserialize(cls,
                    data: dict,
                    save: bool = False) -> 'Person':
        """
        Deserialize a dictionary with format:
        {
            "first_name": "Liam",
            "last_name": "Surname",
            "age": 28
        }
        And create an object Person with it

        To save the instance in the database then send the save option to True

        :param data: serialize dict with the data for the Person object
        :type data: dict
        :param save: says if need to perform the save into the database
        :type save: bool
        :return: Person object
        """
        person = Person(
            guid=data.get('guid') if data.get('guid') else None,
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            age=data.get('age')
        )

        if save:
            person.guid = person.save()

        return person

        # for first_name, last_name, age in zip(first_names, last_names, ages):
        #     doc = Person(
        #         first_name=data.get('first_name'),
        #         last_name=data.get('last_name'),
        #         age=data.get('age')
        #     )
        #     docs.append(doc.serialize())
        # result = collection.insert_many(docs)
        # return result.inserted_ids

    def serialize(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

    def save(self) -> str:
        """
        :return: inserted id
        """
        collection = get_nosql()[self.__collection__]
        result = collection.insert_one(self.serialize())
        return result.inserted_id

    @classmethod
    def save_many(cls, persons: []) -> list:
        """
        :param persons: list of serialized Persons' objects
        :type persons: list
        :return: list of inserted ids
        """
        collection = get_nosql()[cls.__collection__]
        result = collection.insert_many(persons)
        return result.inserted_ids
