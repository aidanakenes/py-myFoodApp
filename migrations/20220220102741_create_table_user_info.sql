-- migrate:up

CREATE TABLE IF NOT EXISTS user_info (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(12),
    email VARCHAR(100)
);

CREATE INDEX index_phone_mail on user_info (
    phone,
    email
);

-- migrate:down

DROP TABLE IF EXISTS user_info CASCADE;