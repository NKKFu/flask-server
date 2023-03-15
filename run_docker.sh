#!/bin/bash

# This script starts or stops the Docker container
if [ "$1" == "up" ]; then
  docker-compose up
  echo "Container started!"
elif [ "$1" == "down" ]; then
  # Stop and remove the container, as well as any volumes and networks created by Docker Compose
  docker-compose down
  echo "Container stopped and removed!"
elif [ "$1" == "res" ]; then
  # Restart the container in detached mode
  docker-compose rm -fs
  docker-compose up --build -d
  echo "Container restarted!"
else
  # Display usage information
  echo "Usage: $0 [up|down|res]"
  exit 1
fi
