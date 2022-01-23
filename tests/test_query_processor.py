import pytest

from literature_searcher.query_processor import process

def test_returns_empty_string_on_invalid_query():
    assert process("") == []

def test_knows_about_shakespeare():
    assert any("playwright" in result for result in process("Shakespeare"))

def test_knows_about_asimov():
    assert any("science fiction" in result for result in process("Asimov"))

def test_knows_about_huxley():
    assert any("biologist" in result for result in process("Homer"))

def test_not_case_sensitive():
    assert any("playwright" in result for result in process("shakespeare"))
