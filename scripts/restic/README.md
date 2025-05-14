# Restic Backup Script

A simple shell script to automate backups using Restic and Rclone with Google Drive.

## Features

- Backs up specified directories to Google Drive using Restic
- Applies retention policy (7 daily, 4 weekly, 6 monthly backups)
- Simple configuration
- Password protection

## Prerequisites

1. **Restic** - A fast, secure, efficient backup program
   ```bash
   # On Debian/Ubuntu
   sudo apt install restic
   
   # On Fedora
   sudo dnf install restic
   
   # On macOS (using Homebrew)
   brew install restic
   ```

2. **Rclone** - For cloud storage access
   ```bash
   # Install rclone (follow instructions for your OS)
   curl https://rclone.org/install.sh | sudo bash
   ```

3. **Google Drive Setup**
   - Run `rclone config` to set up Google Drive
   - Follow the interactive setup to authenticate with your Google account
   - Name your remote (e.g., `googledrive`)

## Installation

1. Clone this repository
   ```bash
   git clone <repository-url>
   cd restic-backup
   ```

2. Make the script executable
   ```bash
   chmod +x resticy.sh
   ```

3. Edit the script to set your password
   ```bash
   nano resticy.sh
   ```
   Change `your_secure_password_here` to your actual password

## Usage

### Basic Usage
```bash
./resticy.sh
```

### Using Environment Variables (Recommended)
Instead of hardcoding your password in the script, you can set it as an environment variable:

```bash
export RESTIC_PASSWORD="your_secure_password_here"
./resticy.sh
```

### What's Backed Up
By default, the script backs up:
- `~/Documents`
- `~/Work`

To change these directories, edit the `restic backup` line in the script.

## Retention Policy
The script keeps:
- 7 daily backups
- 4 weekly backups
- 6 monthly backups

Older backups are automatically pruned.

## Security Notes

- **Never commit your actual password to version control**
- Consider using a password manager for your backup password
- The script includes a check to prevent running with the default password

## Troubleshooting

### Common Issues

1. **Rclone not configured**
   ```
   Error: Failed to create file system for "googledrive:restic-backups": didn't find section in config file
   ```
   Solution: Run `rclone config` and set up your Google Drive remote

2. **Permission denied**
   ```
   open /path/to/file: permission denied
   ```
   Solution: Make sure the script has read access to the files you're trying to back up

3. **Repository not found**
   ```
   Fatal: unable to open config file: <config/> does not exist
   ```
   Solution: The repository needs to be initialized first. Run:
   ```bash
   restic -r rclone:googledrive:restic-backups init
   ```

## License

This project is open source and available under the [MIT License](LICENSE).
