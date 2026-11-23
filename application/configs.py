# -*- coding: utf-8 -*-
import os

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config(object):
    SECRET_KEY = '^753*&FdFS#4D'
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('POSTGRES_USER', 'postgres')}:"
        f"{os.getenv('POSTGRES_PASSWORD', 'postgres')}@"
        f"{os.getenv('POSTGRES_HOST', 'db')}:"
        f"{os.getenv('POSTGRES_PORT', '5432')}/"
        f"{os.getenv('POSTGRES_DB', 'todo_db')}"
    )


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = DevelopmentConfig.SQLALCHEMY_DATABASE_URI


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}