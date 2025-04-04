# Unique Password Generator

## Overview
Generates strong, random passwords while ensuring uniqueness across existing records. Useful for secure credential creation.

## Libraries Used
- `random`
- `string`
- `cryptography.fernet`
- `mysql.connector`
- `json`
- `pickle`
- `os`

## Concept
The tool creates cryptographically secure passwords and checks for duplicates by comparing encrypted values before finalizing a password.

## Files
- [passwd_generator.py](./passwd_generator.py) – core logic
- [backup_passwd.py](./backup_passwd.py) – backup generated password
- [README.md](./README.md)