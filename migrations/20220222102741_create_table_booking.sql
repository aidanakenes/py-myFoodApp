-- migrate:up

CREATE TABLE IF NOT EXISTS booking (
    uid SERIAL PRIMARY KEY,
    booking_id uuid,
    price INT,
    user_id INT REFERENCES user_info (user_id)
    offer_details_id INT REFERENCES offer_details (offer_details_id)
);

-- migrate:down

DROP TABLE IF EXISTS booking;