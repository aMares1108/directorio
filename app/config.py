from os import getenv
class Config:
    SQLALCHEMY_DATABASE_URI = getenv('MYSQL_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
