#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_restplus import Api
import logging
from logging.handlers import RotatingFileHandler


def create_app(name):
    app = Flask(name)
    api = Api(app)

    config = os.environ.get('CONFIG_ENV', 'config.DevelopmentConfig')
    app.config.from_object(config)
    
    app.logger = logging.getLogger(name)
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

    return app, api
