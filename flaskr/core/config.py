import os


class Config:
    SECRET_KEY: str = os.environ.get("SECRET_KEY")  # Flask-Core
    DEBUG: bool = False  # Flask-Core
    TESTING: bool = False  # Flask-Core
    JSON_SORT_KEYS: bool = False  # Flask-Core
    MAX_CONTENT_LENGTH: int = 33_554_432  # Flask-Core

    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False  # SQLAlchemy
    SQLALCHEMY_ECHO: bool = False  # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

    FLASK_MIGRATE_TABLE: str = "alembic_version"  # Flask-Migrate

    MAIL_SERVER: str = os.environ.get("MAIL_SERVER") or None  # Flask-Mail
    MAIL_PORT: int = int(os.environ.get("MAIL_PORT") or 587)  # Flask-Mail
    MAIL_USE_SSL: bool = True  # Flask-Mail
    MAIL_USERNAME: str = os.environ.get("MAIL_USERNAME") or None  # Flask-Mail
    MAIL_PASSWORD: str = os.environ.get("MAIL_PASSWORD") or None  # Flask-Mail

    CACHE_TYPE: str = os.environ.get("CACHE_TYPE") or "simple"  # Flask-Cache
    CACHE_REDIS_URL: str = os.environ.get("REDIS_URL") or None  # Flask-Cache


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


config_by_name = {"development": DevelopmentConfig}
