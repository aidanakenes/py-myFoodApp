import json


class Booking:

    def __init__(self, raw_data):
        self.booking_id = raw_data.get('booking_id') if raw_data.get('id') is None else raw_data.get('id')
        self.phone = raw_data.get('phone')
        self.email = raw_data.get('email')
        self.offer = raw_data.get('offer') if raw_data.get('details') is None else json.loads(raw_data.get('details'))
        self.passengers = raw_data.get('passengers') if raw_data.get('info') is None else json.loads(
            raw_data.get('info'))

    def __dict__(self):
        return {
            'id': self.booking_id,
            'phone': self.phone,
            'email': self.email,
            'offer': self.offer,
            'passengers': self.passengers
        }


class Offer:

    def __init__(self, raw_data):
        self.offer_id = raw_data.get('offer_id') if raw_data.get('id') is None else raw_data.get('id')
        self.title = raw_data.get('title') if raw_data.get('title') is None else raw_data.get('title')
        self.price = raw_data.get('price') if raw_data.get('price') is None else raw_data.get('price')

    def __dict__(self):
        return {
            'id': self.offer_id,
            'title': self.title,
            'price': self.price
        }


class User:

    def __init__(self, raw_data):
        self.user_id = raw_data.get('user_id') if raw_data.get('user_id') is None else raw_data.get('user_id')
        self.name = raw_data.get('name') if raw_data.get('name') is None else raw_data.get('name')
        self.phone = raw_data.get('phone') if raw_data.get('phone') is None else raw_data.get('phone')
        self.email = raw_data.get('email') if raw_data.get('email') is None else raw_data.get('email')
