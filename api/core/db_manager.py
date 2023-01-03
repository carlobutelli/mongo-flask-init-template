#!/usr/bin/env python3
from flask import g, current_app as app
from pymongo import MongoClient

from api.exceptions import MongoDBNotConfigure

# ---------------------------------------------------- #
#                  NoSQL Manager                       #
# ---------------------------------------------------- #
def get_nosql():
    """Return the NoSQL database for the app, it will create it if is needed
    :return: A MongoDatabase
    :rtype: pymongo.database.Database
    """

    if "db" not in g:
        if (
                "MONGODB_DATABASE_HOST" not in app.config or
                "MONGODB_USER" not in app.config or
                "MONGODB_USER_PASSWORD" not in app.config or
                "MONGODB_DATABASE" not in app.config
        ):
            raise MongoDBNotConfigure
        print("HOST: ", app.config["MONGODB_DATABASE_HOST"])
        client = MongoClient(app.config["MONGODB_DATABASE_HOST"],
                             username=app.config["MONGODB_USER"],
                             password=app.config["MONGODB_USER_PASSWORD"])

        g.db = client.get_database(app.config["MONGODB_DATABASE"])

    return g.db
