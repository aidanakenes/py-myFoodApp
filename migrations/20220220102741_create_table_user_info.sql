-- migrate:up

CREATE TABLE IF NOT EXISTS user_info (
    uid SERIAL PRIMARY KEY,
    user_id uuid,
    name VARCHAR(100),
    phone VARCHAR(12),
    email VARCHAR(100)
);

CREATE INDEX index_phone_mail on booking (
    phone,
    email
);

-- migrate:down

DROP TABLE IF EXISTS booking;