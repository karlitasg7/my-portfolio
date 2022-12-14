from flask import current_app, url_for
from flask_testing import TestCase

from app import app


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_hello_get(self):
        response = self.client.get(url_for('submit_form'))

        self.assert_200(response)
