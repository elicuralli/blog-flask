import pymysql

class Config:
    DEBUG = True
    TESTING = True

#config bd 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI= "mysql+pymysql://root:admin@localhost/blog_db"

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    SECRET_KEY = 'gatico'
    DEBUG = True
    TESTING = True






