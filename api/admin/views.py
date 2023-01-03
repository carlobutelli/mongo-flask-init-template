#!/usr/bin/env python3
from flasgger import swag_from
from flask import Blueprint, request

from api.admin.handler import check_services

admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.route("/healthcheck")
@swag_from("/api/docs/healthcheck.yml")
def healthcheck():
    if request.method == "GET":
        return check_services()
