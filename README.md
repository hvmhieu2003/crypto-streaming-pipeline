# 🚀 Real-time Crypto Pipeline

Hệ thống Streaming End-to-End thu thập, xử lý và phân tích giá Bitcoin theo thời gian thực sử dụng kiến trúc Medallion (Bronze/Silver/Gold).

## 🏗 Kiến trúc hệ thống
**Binance API** (Websocket) -> **Python Producer** -> **Postgres** (OLTP) -> **Debezium** (CDC) -> **Kafka** -> **ClickHouse** (OLAP) -> **Grafana** (Visualization)



## 🛠 Tech Stack
- **Ingestion:** Python (Websocket), Postgres (OLTP).
- **CDC:** Debezium (Change Data Capture).
- **Message Broker:** Kafka (KRaft mode).
- **Data Warehouse:** ClickHouse (Columnar Storage).
- **Orchestration:** Airflow (Monitoring & Data Quality).
- **Visualization:** Grafana (Real-time Dashboards).
- **Infrastructure:** Docker & Docker Compose.

## 🌟 Tính năng nổi bật
- **Real-time CDC:** Sử dụng Debezium để bắt sự thay đổi dữ liệu từ Postgres WAL, đảm bảo tính nhất quán giữa tầng giao dịch và tầng phân tích mà không gây tải cho Database nguồn.
- **Medallion Architecture:** Dữ liệu được tinh lọc qua 3 tầng trong ClickHouse:
  - **Bronze:** Lưu trữ dữ liệu thô (Raw JSON) trực tiếp từ Kafka.
  - **Silver:** Dữ liệu đã được trích xuất (Flatten) và định dạng chuẩn (Materialized View).
  - **Gold:** Dữ liệu tổng hợp (Aggregate) giá trung bình, cao nhất, thấp nhất theo từng phút sử dụng `AggregatingMergeTree`.
- **Infrastructure as Code:** Toàn bộ hạ tầng được đóng gói qua Docker, tự động khởi tạo Schema và Connector khi startup.

## 📊 Dashboard Preview
<img width="1539" height="631" alt="image" src="https://github.com/user-attachments/assets/98a73d42-7824-42af-97c5-4ac73c449bf8" />

- **Real-time Candlestick Chart:** Biến động giá mở/đóng/cao/thấp.
- **Ingestion Volume:** Theo dõi lưu lượng sự kiện xử lý (Events/min).

## 🚀 Hướng dẫn cài đặt
1. **Clone project:**
   ```bash
   git clone https://github.com/hvmhieu2003/crypto-streaming-pipeline.git
   ```
2. **Cấu hình môi trường**
3. **Khởi động hệ thống:**
   ```bash
   docker-compose up -d
   ```
4. **Truy cập các dịch vụ:**
   - Kafka UI: http://localhost:8095
   - Airflow: http://localhost:13005
   - Grafana: http://localhost:3000
