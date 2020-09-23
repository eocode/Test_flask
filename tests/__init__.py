"""
Init test env
"""
from app.configurations.config import TestingConfig
from app import create_app
import pytest
import os


@pytest.fixture
def app():
    """Create example instance"""
    os.environ["environment_execution"] = "testing"
    microservice = create_app(TestingConfig)
    return microservice


@pytest.fixture
def client(app):
    """Create client instance"""
    return app.test_client()
