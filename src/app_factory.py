#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_restplus import Api
import logging
from logging.handlers import RotatingFileHandler
from src.resources.resources import setup_resources


def setup_config(app):
    config = os.environ.get('CONFIG_ENV', 'config.DevelopmentConfig')
    app.config.from_object(config)

    def get_config_or_default(config_key, default_value):
        return app.config[config_key] if config_key in app.config else default_value

    app.config.get_config_or_default = get_config_or_default


def setup_logger(app, logger_name):
    app.logger = logging.getLogger(logger_name)
    if 'LOG_LEVEL' in app.config:
        app.logger.setLevel(app.config['LOG_LEVEL'])

    handler = RotatingFileHandler(
        app.config['LOG_FILENAME'],
        maxBytes=app.config['LOG_MAX_BYTES'],
        backupCount=app.config['LOG_BACKUP_COUNT']
    )
    app.logger.addHandler(handler)

    if 'LOG_FORMAT' in app.config:
        formatter = logging.Formatter(app.config['LOG_FORMAT'])
        handler.setFormatter(formatter)


def setup_api(app):
    version = app.config.get_config_or_default('VERSION', '1.0')
    title = app.config.get_config_or_default('TITLE', 'Honeycomb')
    description = app.config.get_config_or_default('DESCRIPTION', '{} api version : {}'.format(title, version))

    app.api = Api(app, version=version, title=title, description=description)


def create_app(name):
    app = Flask(name)
    
    setup_config(app)
    setup_logger(app, name)
    setup_api(app)
    # Gather resources from the src/resources/resources.py
    setup_resources(app.api)

    return app
