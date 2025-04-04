# Password Vault

## Overview
A command-line password manager using encrypted storage, master key protection, and optional backup.

## Libraries Used
- `cryptography.fernet`
- `mysql.connector`
- `os`
- `json`
- `pickle`
- `random`

## Concept
Encrypts passwords using Fernet before storing in a MySQL database. Uses environment variables for secure key access. Supports encrypted backups.

## Files
- [manager.py](./manager.py) – main interface
- [backup_passwd.py](./backup_passwd.py) - create backup
- [README.md](./README.md)