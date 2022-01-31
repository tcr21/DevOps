import pytest
import unittest
import requests
from flask import current_app
from literature_searcher import create_app

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['WTF_CSRF_ENABLED'] = False # no CSRF during tests
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.appctx.pop()
        self.app = None
        self.appctx = None
        self.client = None

    def test_app(self):
        assert self.app is not None
        assert current_app == self.app

    def test_search_page_redirect(self):
        # Test if home page is search page
        response = self.client.get('/', follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == '/'

        # Test for different fields in html
        html = response.get_data(as_text=True)
        assert 'name="search_query"' in html
        assert 'name="file_type"' in html
        assert 'value="html"' in html
        assert 'value="md"' in html
        assert 'value="pdf"' in html

    def test_search_result_redirect(self):        
        post_response = self.client.post('/search_result', query_string={
            'search_query': 'shakespeare',
            'file_type': 'html',
        }, follow_redirects=True)
        
        assert post_response.status_code == 200
        assert post_response.request.path == '/search_result' # redirected to search_result