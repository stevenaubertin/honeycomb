#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from app_factory import create_app
from flask_restplus import Resource, Api

app, api = create_app(__name__)


@api.route('/')
class Index(Resource):
    def get(self):
        return json.dumps({'success': 'TODO'})


if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
