-- 1. Pipeline từ Kafka sang Silver
CREATE MATERIALIZED VIEW IF NOT EXISTS bitcoin_prices_mv TO bitcoin_prices_silver AS
SELECT
    JSONExtractString(payload, 'after', 'symbol') AS symbol,
    JSONExtractFloat(payload, 'after', 'price') AS price,
    JSONExtractInt(payload, 'after', 'timestamp') AS timestamp
FROM bitcoin_prices_kafka;

-- 2. Pipeline từ Silver sang Gold
CREATE MATERIALIZED VIEW IF NOT EXISTS bitcoin_prices_gold_mv TO bitcoin_prices_gold AS
SELECT
    toStartOfMinute(ingested_at) AS window_start,
    symbol,
    avg(price) AS avg_price,
    max(price) AS max_price,
    min(price) AS min_price,
    countState(*) AS total_trades
FROM bitcoin_prices_silver
GROUP BY window_start, symbol;