import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/biblioteca'  
    SQLALCHEMY_TRACK_MODIFICATIONS = False