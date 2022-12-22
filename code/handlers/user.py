from sanic import Sanic, response

import json

from code import db


async def sign_up(request):
    user_id = await db.create_user(request.app.ctx.db_pool, request.json)

    return response.json({"user_id": user_id}, dumps=json.dumps, default=str)
