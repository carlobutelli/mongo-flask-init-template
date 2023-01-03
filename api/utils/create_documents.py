from pymongo.collection import Collection


def create_documents(collection: Collection) -> list:
    first_names = ["Carlo", "Andres", "Luca", "Santos", "Liam"]
    last_names = ["Rusha", "Smith", "Parker", "Doris", "Adam"]

    ages = [38, 35, 32, 40, 41, 46]

    docs = []

    for first_name, last_name, age in zip(first_names, last_names, ages):
        doc = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age
        }
        docs.append(doc)

    result = collection.insert_many(docs)
    return result.inserted_ids
