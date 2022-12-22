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
        'offer_id': {
            'type': 'string'
        },

    },
    'required': [
        'offer_id'
    ]
}

