"""
Initialized example
"""

from flask import Flask
from dotenv import load_dotenv
from app.database.db_instance import db
from flask_migrate import Migrate
from os import environ

# Modules
from modules.example.view import example
from modules.api.v1.view import api_v1

# Custom configuration environments
from app.configurations.config import config

# Load env variables
load_dotenv(".env")


def create_app(environment):
    """Basic modularized example configuration"""
    application = Flask(__name__)

    application.config.from_object(environment)

    # Start application with context app
    with application.app_context():
        # Docs for Flask Blueprints: https://flask.palletsprojects.com/en/1.1.x/blueprints/
        application.register_blueprint(example)
        application.register_blueprint(api_v1)
        db.init_app(application)
        Migrate(application, db)
        db.create_all()

    return application


# Create example
env = config[environ.get('environment_execution')]
microservice = create_app(env)
