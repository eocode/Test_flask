"""
Init test env
"""
from app import microservice
import os
import pytest


@pytest.fixture
def app():
    """Create example instance"""
    os.environ["environment_execution"] = "testing"
    return microservice


@pytest.fixture
def client(app):
    """Create client instance"""
    return app.test_client()
