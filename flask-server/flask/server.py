import logging
import time
import uuid

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({'id': str(uuid.uuid4()), 'time': int(time.time())})


if __name__ == '__main__':
    log = logging.getLogger('werkzeug')
    log.disabled = True
    app.run(host='0.0.0.0', port=8080, debug=False)
