import pytest
import unittest
import requests
from flask import current_app
from literature_searcher import create_app
from literature_searcher.query_processor import process



class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.appctx = self.app.app_context()
        self.appctx.push()

    def tearDown(self):
        self.appctx.pop()
        self.app = None
        self.appctx = None

    def test_app(self):
        assert self.app is not None
        assert current_app == self.app

    def test_home_page_redirect(self):
        # Sends a GET request to top-level URL of application
        r = requests.get('http://localhost:5000/')
        assert(r.status_code == 200)

        # Test for different fields in html
        text = r.text
        assert 'name="search_query"' in text
        assert 'name="file_type"' in text
        assert 'value="html"' in text
        assert 'value="md"' in text
        assert 'value="pdf"' in text