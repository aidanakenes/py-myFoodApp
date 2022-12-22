-- migrate:up

CREATE TABLE IF NOT EXISTS offer_details (
    offer_details_id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    price INT,
    details json
);

-- migrate:down

DROP TABLE IF EXISTS offer_details CASCADE;