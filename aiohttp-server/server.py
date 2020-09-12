import asyncio
import time
import uuid

import uvloop
from aiohttp import web

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    return web.json_response(
        {'id': str(uuid.uuid4()), 'time': int(time.time())}
    )


app = web.Application()
app.add_routes(routes)
web.run_app(app, host='0.0.0.0', port=8080)
