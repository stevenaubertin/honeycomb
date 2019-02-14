#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from flask import request
from app_factory import create_app

app = create_app(__name__)


@app.route('/', methods=['GET'])
def index():
    return json.dumps({'success': 'TODO'})


if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['FLASK_DEBUG'])
