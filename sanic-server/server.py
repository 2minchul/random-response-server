import asyncio
import time
import uuid

import uvloop
from sanic import Sanic
from sanic import response

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
app = Sanic(__name__)


@app.route("/")
async def test(request):
    return response.json({'id': str(uuid.uuid4()), 'time': int(time.time())})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
