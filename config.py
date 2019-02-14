#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging


class Config(object):
    """Base class for configuration"""
    ENV = 'development'
    DEBUG = False
    TESTING = False
    LOG_FILENAME = 'app.log'
    LOG_MAX_BYTES = 10000
    LOG_BACKUP_COUNT = 1
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    HOST = "0.0.0.0"
    PORT = os.environ.get('PORT', 5000)
    SECRET_KEY = None


class ProductionConfig(Config):
    """Production configuration"""
    ENV = 'production'


class DevelopmentConfig(Config):
    """Development configuration"""
    ENV = 'development'
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class TestingConfig(Config):
    """Testing configuration"""
    ENV = 'test'
    TESTING = True
