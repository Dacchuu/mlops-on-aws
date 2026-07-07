#!/bin/bash

set -e

VERSION=$(cat VERSION)

IMAGE_NAME="mlops-api:${VERSION}"

echo "Deploying version: ${IMAGE_NAME}"


echo "Stopping old container..."

docker stop mlops-container || true

docker rm mlops-container || true


echo "Building Docker image..."

docker build -t ${IMAGE_NAME} .


echo "Starting new container..."

docker run -d \
-p 8000:8000 \
--name mlops-container \
${IMAGE_NAME}


echo "Deployment completed!"

docker ps
