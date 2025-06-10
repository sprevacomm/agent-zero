#!/bin/bash

# Agent Zero Custom Docker Runner
# This script runs your custom Agent Zero Docker image

echo "🚀 Starting Agent Zero Custom..."
echo "📦 Using image: devopsone808/agent-zero-custom:latest"
echo "🌐 Web UI will be available at: http://localhost:50001"
echo ""

# Create data directory if it doesn't exist
if [ ! -d "./agent-zero-data" ]; then
    echo "📁 Creating data directory..."
    mkdir -p ./agent-zero-data
fi

# Pull the latest version
echo "📥 Pulling latest image..."
docker pull devopsone808/agent-zero-custom:latest

# Run the container
echo "▶️  Starting container..."
docker run -it --rm \
    -p 50001:80 \
    -v "$(pwd)/agent-zero-data:/a0" \
    --name agent-zero-custom \
    devopsone808/agent-zero-custom:latest

echo "🛑 Agent Zero stopped." 