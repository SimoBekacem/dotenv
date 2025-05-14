#!/bin/bash

# Configuration - Replace with your actual values before using
echo "Note: You should configure rclone and set your password before using this script"

export RCLONE_CONFIG="$HOME/.config/rclone/rclone.conf"
export RESTIC_REPOSITORY="rclone:googledrive:restic-backups"
# Set your actual password here or use an environment variable
export RESTIC_PASSWORD="your_secure_password_here"

# Check if password is set
if [ "$RESTIC_PASSWORD" = "your_secure_password_here" ]; then
    echo "ERROR: Please set your RESTIC_PASSWORD before running this script"
    exit 1
fi

# Run backup
restic backup ~/Documents ~/Work

# Apply retention policy
restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 6 --prune
