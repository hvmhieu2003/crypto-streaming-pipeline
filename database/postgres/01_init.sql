CREATE TABLE IF NOT EXISTS bitcoin_prices (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(20),
    price DECIMAL,
    timestamp BIGINT
);