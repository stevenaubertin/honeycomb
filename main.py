import json
from flask import request
from app_factory import create_app

app = create_app(__name__)


@app.route('/', methods=['GET'])
def index():
    return json.dumps({'success': 'TODO'})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
