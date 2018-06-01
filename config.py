# -*- coding: utf-8 -*-
# Author: HaifengMay
# Function: 
# Date: '2018-05-03'

class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    # SQLALCHEMY_ECHO = True
