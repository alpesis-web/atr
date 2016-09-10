import json
import unittest

import settings.testing
from utils.sqlalchemy import db
from apiserver.apiserver import api_server

class APIServerTestMixin(unittest.TestCase):

    def setUp(self):
        self.server = api_server(custom_settings=settings.testing)
        self.client = self.server.test_client()
       
    def tearDown(self):
        with self.server.app_context():
            db.drop_all()

    def test_config_settings(self):
        config = self.server.config
        self.assertEquals(config['SQLALCHEMY_DATABASE_URI'], 'sqlite:///test.db')
        self.assertEquals(config['TESTING'], True)
        self.assertEquals(config['DEBUG'], True)
