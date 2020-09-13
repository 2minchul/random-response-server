import asyncio
import time
import uuid

import sanic.log
import uvloop
from sanic import Sanic
from sanic import response

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

log_config = sanic.log.LOGGING_CONFIG_DEFAULTS
del log_config['loggers']['sanic.access']

app = Sanic(__name__, log_config=log_config)


@app.route("/")
async def test(request):
    return response.json({'id': str(uuid.uuid4()), 'time': int(time.time())})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False, access_log=False)
