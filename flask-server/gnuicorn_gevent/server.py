import time
import uuid

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({'id': str(uuid.uuid4()), 'time': int(time.time())})
