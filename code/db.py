import uuid
from datetime import datetime
import json

from code.helpers.decorators import with_connection
from code import models


@with_connection
async def create_booking(booking, *args, **kwargs):
    conn = kwargs.pop('connection')

    booking_id = await _insert_booking(conn, booking)

    return get_booking(booking_id)


async def _insert_booking(conn, booking):
    stmt = """INSERT INTO booking (booking_id, user_id, offer_details_id, price)
            VALUES ($1, $2, $3, $4) RETURNING booking_id;"""

    booking_id = str(uuid.uuid4())

    uid = await conn.fetchval(
        stmt, booking_id, booking['user_id'], booking['offer_details_id'], booking['price'])

    return uid


@with_connection
async def get_booking(booking_id, *args, **kwargs):
    conn = kwargs.pop('connection')

    booking_data = await _select_booking(conn, booking_id)

    return booking_data


@with_connection
async def get_offers(search_pattern, *args, **kwargs):
    conn = kwargs.pop('connection')

    booking_data = await _select_offers(conn, search_pattern)

    return booking_data


async def _select_offers(conn, search_pattern):
    stmt = """SELECT * 
            FROM offers o
            WHERE o.title LIKE '%$1%'"""

    booking_records = await conn.fetchrow(stmt, search_pattern)

    return models.Offer(booking_records)


async def _select_booking(conn, booking_id):
    stmt = """SELECT * 
            FROM booking b
            INNER JOIN offer_details od ON b.offer_details_id=od.offer_details_id 
            WHERE b.booking_id=$1"""

    booking_records = await conn.fetchrow(stmt, booking_id)

    return models.Booking(booking_records)


@with_connection
async def get_bookings(email, phone, *args, **kwargs):
    conn = kwargs.pop('connection')
    stmt = """SELECT b.booking_id, b.phone, b.email, od.details, b.passengers 
            FROM booking b 
            INNER JOIN offer_details od ON b.offer_details_id=od.offer_details_id 
            WHERE b.email=$1 AND b.phone=$2;"""

    rows = await conn.fetch(stmt, email, phone)

    bookings = []
    for row in rows:
        bookings.append(models.Booking(row))

    return bookings
