from flaskAppServer import create_app

import pytest

def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing
