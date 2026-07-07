#!/bin/bash

set -e

echo "Stopping old container..."

docker stop mlops-container || true

docker rm mlops-container || true


echo "Starting new container..."

docker run -d \
-p 8000:8000 \
--name mlops-container \
mlops-api


echo "Deployment completed!"

docker ps
