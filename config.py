#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Config(object):
    """Base class for configuration"""
    DEBUG = False
    TESTING = False
    LOG_FILENAME = 'log'
    LOG_MAX_BYTES = 10000
    LOG_BACKUP_COUNT = 1
    LOG_LEVEL = ['INFO', 'ERROR']
    HOST = "0.0.0.0"
    PORT = 5000


class ProductionConfig(Config):
    """Production configuration"""
    pass


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    LOG_LEVEL = ['INFO', 'ERROR', 'DEBUG']


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
