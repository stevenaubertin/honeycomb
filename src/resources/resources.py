#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_restplus import Resource, Api

def setup_resources(api):
    @api.route('/hello')
    class HelloWorld(Resource):
        def get(self):
            return {'hello': 'world'}