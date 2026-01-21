#!/bin/sh

echo "Waiting for Debezium to be ready..."
# Chờ cho đến khi Debezium API phản hồi 200
while [ $(curl -s -o /dev/null -w "%{http_code}" http://debezium:8083/connectors) -ne 200 ]; do
  sleep 2
done

echo "Registering Postgres connector..."
curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" \
    http://debezium:8083/connectors/ -d @/init-scripts/postgres-connector.json

echo "Done!"