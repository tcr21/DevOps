import pytest
import unittest
from flask import current_app
from literature_searcher import create_app

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.appctx.pop()
        self.app = None
        self.appctx = None

    def test_app(self):
        assert self.app is not None
        assert current_app == self.app

    def test_home_page_redirect(self):
        # Test if home page is search page
        r = self.client.get('/', follow_redirects=True)
        assert r.status_code == 200

        # Test for different fields in html
        html = r.get_data(as_text=True)
        assert 'name="search_query"' in html
        # assert 'name="file_type"' in html
        # assert 'value="html"' in html
        # assert 'value="md"' in html
        # assert 'value="pdf"' in html
