import pytest

from literature_searcher.query_processor import process

def test_returns_empty_string_on_invalid_query():
    assert process("") == []
