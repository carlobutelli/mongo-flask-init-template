#!/usr/bin/env python3
from flask import jsonify, g

from api import get_nosql
from api.core.logs import log_debug_with_txn_id, log_error_with_txn_id


def check_services():
    response = {}
    service = None
    try:
        service = "MongoDB"
        get_nosql()
        log_debug_with_txn_id("[HEALTH-CHECK]", g.transaction_id, f"{service} is healthy")
        response[service] = {"healthy": True}

    #     other services to be checked
    except Exception as e:
        log_error_with_txn_id("[HEALTH-CHECK]",
                              g.transaction_id,
                              f"service {service} returned unhealthy healthcheck: {e}")
        response[service] = {
            "healthy": False,
            "message": f"Error: {e}"
        }
        return jsonify(response), 500
    else:
        return jsonify(response), 200
