import psycopg2
import websocket
import json
import os

# Lấy thông tin từ .env hoặc để mặc định
conn = psycopg2.connect(
    host="postgres-main",
    port="5432",
    database="crypto_db",
    user="myuser",
    password="mypassword"
)
cur = conn.cursor()

# Tạo table nếu chưa có
cur.execute("""
    CREATE TABLE IF NOT EXISTS bitcoin_prices (
        id SERIAL PRIMARY KEY,
        symbol VARCHAR(20),
        price DECIMAL,
        timestamp BIGINT
    );
""")
conn.commit()

def on_message(ws, message):
    data = json.loads(message)
    cur.execute(
        "INSERT INTO bitcoin_prices (symbol, price, timestamp) VALUES (%s, %s, %s)",
        (data['s'], float(data['p']), data['E'])
    )
    conn.commit()
    print(f"Inserted to Postgres: {data['s']} - {data['p']}")

ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/btcusdt@trade", on_message=on_message)
ws.run_forever()