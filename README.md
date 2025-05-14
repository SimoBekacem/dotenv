# Dotenv Configuration

This repository contains my personal configuration files, including:

- `.bashrc` - My bash configuration
- `.config/nvim/` - My Neovim configuration
- `.tmux.conf` - My tmux configuration

## Usage

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

## Note

This repository contains personal configuration files. Use them as a reference, but be aware that they are tailored to my personal setup.

## Repository Information

- **Owner**: SimoBekacem
- **Repository**: [dotenv](https://github.com/SimoBekacem/dotenv)
- **Last Updated**: May 14, 2025
