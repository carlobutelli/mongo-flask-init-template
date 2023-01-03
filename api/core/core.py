#!/usr/bin/env python3
from .db_manager import get_nosql


class Core:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    @staticmethod
    def init_app(app):
        with app.app_context():
            get_nosql()
