import json

from flasgger import swag_from
from flask import Blueprint, g, jsonify, current_app as app

from api.core.logs import log_info_with_txn_id
from api.mongo.models import Person

mongo = Blueprint("mongo", __name__)


@mongo.route("/users", methods=['POST'])
@swag_from("/api/docs/add_users.yml")
def live_test_ping():
    log_info_with_txn_id("[MONGO]", g.transaction_id, "got new request for mongo")

    print("HOST: ", app.config["MONGODB_DATABASE_HOST"])
    print("USER: ", app.config["MONGODB_USER"])
    print("USER_PWD: ", app.config["MONGODB_USER_PASSWORD"])
    print("DATABASE: ", app.config["MONGODB_DATABASE"])

    first_names = ["AAAA", "BBBB", "CCCC", "DDDD", "EEEE"]
    last_names = ["Rusha", "Smith", "Parker", "Doris", "Adam"]

    ages = [38, 35, 32, 40, 41, 46]

    data = []

    for first_name, last_name, age in zip(first_names, last_names, ages):
        object = Person(
            first_name=first_name,
            last_name=last_name,
            age=age
        )
        data.append(object.serialize())

    inserted_ids = Person.save_many(data)

    return jsonify(ids=json.dumps(inserted_ids, default=str)), 200
