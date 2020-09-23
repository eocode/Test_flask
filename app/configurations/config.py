"""Flask configurations"""
from os import environ


class Config:
    """Set common configuration"""
    SECRET_KEY = environ.get("SECRET_KEY")


class PgConfig:
    """Configurations for production database
    See configurations here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
    """
    SQLALCHEMY_DATABASE_URI = f"postgresql://{environ.get('DB_USER')}:{environ.get('DB_PASSWORD')}@{environ.get('DB_HOST')}:{environ.get('DB_PORT')}/{environ.get('DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config, PgConfig):
    """Configuration for development with implement basic config and postgresql configuration"""
    DEBUG = True


class ProductionConfig(Config, PgConfig):
    """Configuration for Production with implement basic config and postgresql configuration"""
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration with sqlite as database"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"


# Dictionary with available environments
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
