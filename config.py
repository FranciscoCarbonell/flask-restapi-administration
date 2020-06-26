import datetime


class Developement:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    UPLOADED_PHOTOS_DEST = "images"
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=1)
    SECRET_KEY = "123456789"


class Production:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    UPLOADED_PHOTOS_DEST = "images"
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=1)
    SECRET_KEY = "123456789"


class Manager:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app/database.db'
