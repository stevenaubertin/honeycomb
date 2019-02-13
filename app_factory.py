#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
import logging
from logging.handlers import RotatingFileHandler


def create_app(name, config='config.ProductionConfig'):
    app = Flask(name)
    app.config.from_object(config)
    
    app.logger = logging.getLogger(name)
    if 'LOG_LEVEL' in app.config:
        app.logger.setLevel(app.config['LOG_LEVEL'])
    
    app.logger.addHandler(RotatingFileHandler(
        app.config['LOG_FILENAME'],
        maxBytes=app.config['LOG_MAX_BYTES'],
        backupCount=app.config['LOG_BACKUP_COUNT']
    ))

    return app
