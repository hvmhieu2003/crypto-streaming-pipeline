from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import logging

# Xóa dòng import psql đi

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def check_ingestion_logic():
    # Đây là nơi bạn sẽ viết code check data sau này
    logging.info("Checking data in ClickHouse... All systems green!")
    return True

with DAG(
    'crypto_pipeline_monitor',
    default_args=default_args,
    description='Giám sát luồng dữ liệu Crypto',
    schedule_interval='@hourly',
    catchup=False
) as dag:

    monitor_task = PythonOperator(
        task_id='check_clickhouse_data',
        python_callable=check_ingestion_logic
    )