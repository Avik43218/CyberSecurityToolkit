# Changelog

All notable changes to this project will be documented in this file.

## [v1.0.0] - 2025-04-05

### Added
- **PasswordVault**: A secure password manager with encryption using `cryptography.fernet`, encrypted backups, and database storage.
- **UniquePasswordGenerator**: Tool to generate unique passwords not present in existing records, with validation and optional backup.
- **SecurePasswordEvaluator**: Password strength analyzer using entropy calculation, brute-force time estimation, and pattern analysis.

### Features
- Encrypted backup support (.json and .dat formats)
- Environment variable usage for key security
- CLI-based interaction for all tools
- GitHub-ready documentation with README and LICENSE

### Planned
- GUI integration for all tools
- Additional tools like keylogger and antivirus scanner
- Software bundle with unified interface

### Notes
- This is a **pre-release** version for testing and feedback.
- Keys and database files are not included for security reasons.
