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
        assert 'type="submit"' in html

    def test_valid_query_search_result_redirect(self):
        # Test post response 
        response = self.client.get('/search_result', query_string={
            'search_query': 'shakespeare'
        })
        assert response.status_code == 200
        assert response.request.path == '/search_result'

        # Test for different fields in html
        html = response.get_data(as_text=True)
        assert 'form action="/download/shakespeare"' in html
        assert 'value=".html"' in html
        assert 'value=".md"' in html
        assert 'value=".pdf"' in html
        assert 'type="submit"' in html 
        assert 'href="/"' in html

    def test_invalid_query_search_result_redirect(self):
        # Test post response 
        response = self.client.get('/search_result', query_string={
            'search_query': ''
        })
        assert response.status_code == 200
        assert response.request.path == '/search_result'

        # Test for different fields in html
        html = response.get_data(as_text=True)
        assert "No match to query!" in html
        assert 'href="/"' in html