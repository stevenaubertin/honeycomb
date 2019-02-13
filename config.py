#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging


class Config(object):
    """Base class for configuration"""
    FLASK_DEBUG = False
    TESTING = False
    LOG_FILENAME = 'app.log'
    LOG_MAX_BYTES = 10000
    LOG_BACKUP_COUNT = 1
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = '%(levelname)s:%(message)s'
    HOST = "0.0.0.0"
    PORT = os.environ.get('PORT', 5000)


class ProductionConfig(Config):
    """Production configuration"""
    pass


class DevelopmentConfig(Config):
    """Development configuration"""
    FLASK_DEBUG = True
    LOG_LEVEL = 'DEBUG'


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
