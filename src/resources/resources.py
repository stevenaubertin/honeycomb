#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask_restplus import Resource, Api

def setup_resources(api):
    @api.route('/About')
    class About(Resource):
        def get(self):
            return {
                'Project': 'Honeycomb',
                'Description': 'A Python, Flask, Swagger, Docker, Rest Boilerplate',
                'From': 'This resource is from src/resources/resources.py',
                'Add': 'You should add resources inside the "setup_resources(api)" function',
                'Maintainer' : 'stevenaubertin'
            }