SEARCH_SCHEMA = {
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'search_pattern': {
            'type': 'string'
        },
        'currency': {
            'type': 'string'
        },
    },
    'required': [
        'search_pattern',
        'currency',
    ]
}

BOOKING_SCHEMA = {
    'type': 'object',
    'additionalProperties': False,
    'properties': {
        'booking_id': {
            'type': 'string'
        },
        'offer_id': {
            'type': 'string'
        },
        'price': {
            'type': 'string'
        },

    },
    'required': [
        'offer_id',
        'phone',
        'email',
        'price',
        'count'
    ]
}

