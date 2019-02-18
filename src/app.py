#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from app_factory import create_app

app = create_app(__name__)

if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
