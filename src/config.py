#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Documentation about configuration can be found : http://flask.pocoo.org/docs/1.0/config

import os
import logging


class Config(object):
    """Base class for configuration"""
    # Environnement
    ENV = 'development'
    DEBUG = False

    # Logger
    LOG_FILENAME = os.environ.get('LOG_FILENAME', 'app.log')
    LOG_MAX_BYTES = 10000
    LOG_BACKUP_COUNT = 1
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    # Api
    TITLE = os.environ.get('TITLE', 'Honeycomb')
    VERSION = os.environ.get('VERSION', '1.0')
    DESCRIPTION = os.environ.get('DESCRIPTION', '{} api version : {}'.format(TITLE, VERSION))

    # Web Server
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = os.environ.get('PORT', 5000)
    """A secret key that will be used for securely signing the session cookie and can be used for any other security 
    related needs by extensions or your application. It should be a long random string of bytes, 
    although unicode is accepted too. For example, copy the output of this to your config:"""
    SECRET_KEY = os.environ.get('SECRET_KEY', None)


class ProductionConfig(Config):
    """Production configuration"""
    # Environnement
    ENV = 'production'


class DevelopmentConfig(Config):
    """Development configuration"""
    # Environnement
    ENV = 'development'
    DEBUG = True

    # Logger
    LOG_LEVEL = logging.DEBUG


class TestingConfig(Config):
    """Testing configuration"""
    # Environnement
    ENV = 'test'
    """Enable testing mode. Exceptions are propagated rather than handled by the the app’s error handlers. 
    Extensions may also change their behavior to facilitate easier testing. You should enable this in your own tests."""
    TESTING = True
