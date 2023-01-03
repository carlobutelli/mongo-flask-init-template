#!/usr/bin/env python3
from api.core.logs import log_error_with_txn_id
from api.exceptions import ValidationError


def validate_data_keys(data: dict, keys: set):
    if not data:
        log_error_with_txn_id("[VALIDATION]", g.transaction_id, "payload data not found")
        raise ValidationError("payload not found", list(keys))

    # check if all the data is present
    if not keys.issubset(data.keys()):
        log_error_with_txn_id("[VALIDATION]", g.transaction_id, "incorrect keys in payload")
        raise ValidationError("missing fields",
                              list(keys - set(data.keys())))


def validate_content_keys(data: dict, keys: set):
    if not data:
        log_error_with_txn_id("[VALIDATION]", g.transaction_id, "payload data not found")
        raise ValidationError("data not found", list(keys))

    # check that all keys are not empty
    for key in keys:
        value = data.get(key)
        if value is None or value is "":
            raise ValidationError("field empty", [key])
