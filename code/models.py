import json


class Booking:

    def __init__(self, raw_data):
        self.booking_id = raw_data.get('booking_id')
        self.phone = raw_data.get('phone')
        self.email = raw_data.get('email')
        self.name = raw_data.get('name')
        self.offer_details_id = raw_data.get('offer_details_id')
        self.title = raw_data.get('title')
        self.price = raw_data.get('price')

    def __dict__(self):
        return {
            'id': self.booking_id,
            'phone': self.phone,
            'email': self.email,
            'name': self.name,
            'offer_details_id': self.offer_details_id,
            'title': self.title,
            'price': self.price
        }


class Offer:

    def __init__(self, raw_data):
        self.offer_id = raw_data.get('offer_details_id')
        self.title = raw_data.get('title')
        self.price = raw_data.get('price')
        self.details = raw_data.get('details')

    def __dict__(self):
        return {
            'id': self.offer_id,
            'title': self.title,
            'price': self.price,
            'details': self.details
        }


class User:

    def __init__(self, raw_data):
        self.user_id = raw_data.get('user_id') if raw_data.get('user_id') is None else raw_data.get('user_id')
        self.name = raw_data.get('name') if raw_data.get('name') is None else raw_data.get('name')
        self.phone = raw_data.get('phone') if raw_data.get('phone') is None else raw_data.get('phone')
        self.email = raw_data.get('email') if raw_data.get('email') is None else raw_data.get('email')
