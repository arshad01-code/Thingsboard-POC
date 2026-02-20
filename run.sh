#!/bin/bash

echo "Loading environment variables..."
export $(grep -v '^#' .env | xargs)

docker build -t iot-simulator .

docker run \
  --env-file .env \
  iot-simulator