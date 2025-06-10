# Custom Agent Zero Deployment

## Overview
This repository has been modified to use a custom Docker image hosted on Docker Hub: `devopsone808/agent-zero-custom:latest`

## What Was Modified

### Core Configuration
- **`agent.py`**: Changed `code_exec_docker_image` from `"frdel/agent-zero-run:development"` to `"devopsone808/agent-zero-custom:latest"`

### Documentation Updates
- **`README.md`**: Updated quick start commands to use custom image
- **`docs/installation.md`**: Updated installation instructions throughout
- **`knowledge/default/main/about/github_readme.md`**: Updated knowledge base

### Added Files
- **`run_custom.sh`**: Convenient script to run the custom Agent Zero deployment
- **`CUSTOM_DEPLOYMENT.md`**: This documentation file

## Quick Start

### Option 1: Use the convenience script
```bash
./run_custom.sh
```

### Option 2: Manual Docker commands
```bash
# Pull the custom image
docker pull devopsone808/agent-zero-custom:latest

# Run with data persistence
docker run -d \
    -p 50001:80 \
    -v "$(pwd)/agent-zero-data:/a0" \
    --name agent-zero-custom \
    devopsone808/agent-zero-custom:latest
```

## Access
- **Web UI**: http://localhost:50001
- **Data Directory**: `./agent-zero-data` (auto-created)

## Features of Custom Image
- Based on the official Agent Zero image
- Includes your custom modifications and enhancements
- Maintained at Docker Hub for easy distribution

## Updating
To update to a newer version of your custom image:

```bash
# Stop the current container
docker stop agent-zero-custom && docker rm agent-zero-custom

# Pull the latest version
docker pull devopsone808/agent-zero-custom:latest

# Run the new version
./run_custom.sh
```

## Building and Pushing Updates
If you need to rebuild and push a new version:

```bash
# Build the new image
docker build -t devopsone808/agent-zero-custom:latest .

# Push to Docker Hub
docker push devopsone808/agent-zero-custom:latest
``` 