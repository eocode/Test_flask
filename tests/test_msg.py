"""
Test cases for elements of the n queens
This file test Board and Queen funcs
"""
from . import app, client
from flask import url_for
from os import environ


def test_pass(app):
    assert environ.get('environment_execution') == 'testing'


def test_msg(app, client):
    response = client.get(url_for('example.example_app'))
    assert response.status_code == 200


def test_api_get_msgs(client):
    response = client.get(url_for('api_v1.get_msgs'))
    assert response.status_code == 200


def test_api_get_msg(client):
    response = client.get(url_for('api_v1.get_msg', id=1))
    assert response.status_code == 200
