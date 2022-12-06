from sanic import response

import json
import uuid

from code import schemas
from code import jsonschema_
from code import cache
from code import db
from code.helpers.helpers import convert_currency


async def search(request):
    await jsonschema_.validate(request.json, schemas.SEARCH_SCHEMA)

    search_id = str(uuid.uuid4())
    db_offers = db.get_offers(request.json.get('search_pattern'))

    currency = request.json.get('currency')
    if currency != 'KZT':
        db_offers = await convert_currency(request, db_offers, currency)

    await cache.save_search_results(request.app.ctx.redis, db_offers, search_id)

    return response.json({'search_id': search_id})


async def search_by_id(request, search_id):
    search_results_by_id = await cache.get_search_results(request.app.ctx.redis, search_id)

    return response.json(search_results_by_id, dumps=json.dumps, default=str)
