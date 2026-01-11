# Raritan

SSH client for interacting with Raritan PDU (Power Distribution Unit) devices.

## Features

- SSH connection via Paramiko
- Interactive shell session handling
- Automatic handling of license/agreement prompts

## Usage

```bash
python raritan_ports.py
```

The script will prompt for:
- IP address
- Username
- Password

## How It Works

1. Establishes SSH connection to Raritan PDU
2. Opens interactive shell session
3. Detects and handles "hit any key to accept" prompts
4. Displays shell output

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install paramiko
```

## Requirements

- Python 3.x
- paramiko
