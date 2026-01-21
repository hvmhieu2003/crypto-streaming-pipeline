-- 1. Bảng đích Silver
CREATE TABLE IF NOT EXISTS bitcoin_prices_silver (
    symbol String,
    price Decimal(18, 8),
    timestamp Int64,
    ingested_at DateTime DEFAULT now()
) ENGINE = MergeTree() ORDER BY (symbol, timestamp);

-- 2. Bảng kết nối Kafka
CREATE TABLE IF NOT EXISTS bitcoin_prices_kafka (
    payload String
) ENGINE = Kafka
SETTINGS 
    kafka_broker_list = 'kafka-broker:19092',
    kafka_topic_list = 'cdc.public.bitcoin_prices',
    kafka_group_name = 'clickhouse_consumer_group',
    kafka_format = 'JSONEachRow';

-- 3. Bảng đích Gold
CREATE TABLE IF NOT EXISTS bitcoin_prices_gold (
    window_start DateTime,
    symbol String,
    avg_price Decimal(18, 8),
    max_price Decimal(18, 8),
    min_price Decimal(18, 8),
    total_trades AggregateFunction(count, Int64)
) ENGINE = AggregatingMergeTree() ORDER BY (window_start, symbol);