# Dotenv Configuration

This repository contains my personal configuration files and scripts, including:

- `.bashrc` - My bash configuration
- `.config/nvim/` - My Neovim configuration
- `.tmux.conf` - My tmux configuration
- `scripts/` - Collection of useful scripts
  - `anacrony/` - Anacron-like task scheduler
  - `docker/` - Docker-related utility scripts

## Usage

### Configuration Files

To use these configurations, you can clone this repository and symlink the files to their appropriate locations:

```bash
# Clone the repository
git clone https://github.com/SimoBekacem/dotenv.git ~/dotenv

# Create symlinks
ln -s ~/dotenv/.bashrc ~/.bashrc
ln -s ~/dotenv/.tmux.conf ~/.tmux.conf
mkdir -p ~/.config
ln -s ~/dotenv/.config/nvim ~/.config/nvim
```

### Scripts

#### Anacrony

Anacrony is an anacron-like task scheduler. To install and use it:

```bash
# Install anacrony
sudo cp ~/dotenv/scripts/anacrony/anacrony.py /usr/local/bin/anacrony
sudo chmod +x /usr/local/bin/anacrony

# Example usage
anacrony --help
```

#### Docker Scripts

Various utility scripts for Docker management are available in the `scripts/docker/` directory.

## Note

This repository contains personal configuration files and scripts. Use them as a reference, but be aware that they are tailored to my personal setup.

## Repository Information

- **Owner**: SimoBekacem
- **Repository**: [dotenv](https://github.com/SimoBekacem/dotenv)
- **Last Updated**: May 14, 2025
