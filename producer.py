import json
import websocket
from kafka import KafkaProducer

# Khởi tạo Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPIC_NAME = 'binance_trades'

def on_message(ws, message):
    data = json.loads(message)
    # Cấu trúc lại dữ liệu gọn nhẹ
    payload = {
        'symbol': data['s'],
        'price': float(data['p']),
        'quantity': float(data['q']),
        'timestamp': data['E']
    }
    producer.send(TOPIC_NAME, value=payload)
    print(f"Pushed to Kafka: {payload}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Closed connection")

# Stream giá BTC/USDT từ Binance
socket = "wss://stream.binance.com:9443/ws/btcusdt@trade"
ws = websocket.WebSocketApp(
    socket, 
    on_message=on_message, 
    on_error=on_error, 
    on_close=on_close
)

if __name__ == "__main__":
    print("Starting Producer...")
    ws.run_forever()