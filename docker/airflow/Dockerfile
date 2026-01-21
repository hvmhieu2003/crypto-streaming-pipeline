FROM apache/airflow:2.7.3
USER root
RUN apt-get update && apt-get install -y git
USER airflow
RUN pip install --no-cache-dir kafka-python websocket-client requests psycopg2-binary