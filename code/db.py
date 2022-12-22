import uuid

from code.helpers.decorators import with_connection
from code import models


@with_connection
async def create_booking(booking, *args, **kwargs):
    conn = kwargs.pop('connection')

    booking_id = await _insert_booking(conn, booking)

    return booking_id


async def _insert_booking(conn, booking):
    stmt = """INSERT INTO booking (user_id, offer_details_id)
            VALUES ($1, $2) RETURNING booking_id;"""
    print(booking)
    uid = await conn.fetchval(stmt, int(booking['user_id']), int(booking['offer_details_id']))

    return uid


@with_connection
async def get_booking(booking_id, *args, **kwargs):
    conn = kwargs.pop('connection')

    booking_data = await _select_booking(conn, booking_id)

    return booking_data


@with_connection
async def get_offers(search_pattern, *args, **kwargs):
    conn = kwargs.pop('connection')

    offers = await _select_offers(conn, search_pattern)

    return offers


async def _select_offers(conn, search_pattern):
    stmt = "SELECT * FROM offer_details o WHERE o.title LIKE '%" + search_pattern + "%'"
    try:
        offers = await conn.fetch(stmt)
    except Exception as e:
        print(100*'?')
        print(e)
        print(100*'?')

    return [models.Offer(o).__dict__() for o in offers]


async def _select_booking(conn, booking_id):
    stmt = """SELECT * 
            FROM booking b
            INNER JOIN offer_details od ON b.offer_details_id=od.offer_details_id 
            INNER JOIN user_info u ON b.user_id=u.user_id 
            WHERE b.booking_id=$1"""

    booking_records = await conn.fetchrow(stmt, int(booking_id))

    return models.Booking(booking_records).__dict__()


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


@with_connection
async def create_user(user, *args, **kwargs):
    conn = kwargs.pop('connection')

    user_id = await _insert_user(conn, user)

    return user_id


async def _insert_user(conn, user):
    stmt = """INSERT INTO user_info (name, phone, email)
            VALUES ($1, $2, $3) RETURNING user_id;"""

    uid = await conn.fetchval(stmt, user['name'], user['phone'], user['email'])

    return uid
