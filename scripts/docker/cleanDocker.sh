#!/bin/bash

# Docker System Cleanup Script
# Removes ALL Docker containers, images, volumes, networks, and unused resources

echo "[1/5] Stopping all running containers..."
docker kill $(docker ps -q) 2>/dev/null

echo "[2/5] Removing all containers..."
docker rm -f $(docker ps -a -q) 2>/dev/null

echo "[3/5] Removing all images..."
docker rmi -f $(docker images -a -q) 2>/dev/null

echo "[4/5] Removing all volumes..."
docker volume rm $(docker volume ls -q) 2>/dev/null

echo "[5/5] Removing all networks (except default ones)..."
docker network rm $(docker network ls -q --filter type=custom) 2>/dev/null

# Optional: Prune everything (including build cache, dangling resources)
echo "[+] Running system prune..."
docker system prune -a --volumes --force

echo ""
echo "✅ Docker cleanup complete!"
echo "Containers: $(docker ps -a -q | wc -l | tr -d ' ')"
echo "Images:     $(docker images -a -q | wc -l | tr -d ' ')"
echo "Volumes:    $(docker volume ls -q | wc -l | tr -d ' ')"
echo "Networks:   $(docker network ls -q | wc -l | tr -d ' ')"
