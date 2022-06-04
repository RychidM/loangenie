import os

secrete_key = os.environ.get('SECRETE_KEY')
userPass = os.environ.get('LOAN_GENIE')
databaseURI = os.environ.get('SQLALCHEMY_DATABASE_URI')
userNAme = os.environ.get('MAIL_USERNAME')


class Config:
    SECRET_KEY = secrete_key
    SQLALCHEMY_DATABASE_URI = databaseURI

    DEBUG = True
    TESTING = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = userNAme
    MAIL_PASSWORD = userPass
    MAIL_DEFAULT_SENDER = userNAme
    MAIL_MAX_EMAILS = None
    MAIL_ASCII_ATTACHMENTS = False



