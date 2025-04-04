# CyberSecurity Toolkit

A collection of beginner-friendly yet powerful tools to help users create, evaluate, and manage secure passwords. Built entirely in Python for educational and practical use.

---

## Projects Included

### 1. [Password Generator](UniquePasswordGenerator/)
A secure password generator that creates random, complex passwords of user-defined length using customizable character sets.

- Supports uppercase, lowercase, numbers, and symbols
- Prevents duplication of existing passwords
- Optional export of generated passwords
- Additionally encrypts the password using AES-128 based encryption

---

### 2. [Password Strength Analyzer](SecurePasswordEvaluator/)
This tool analyzes the strength of user-entered passwords using **entropy**, **brute-force time estimation**, and **pattern detection**.

- Entropy-based strength scoring
- Time-to-crack estimation (brute-force)
- Password complexity insights

---

### 3. [Password Manager](PasswordVault/)
A local password manager that stores encrypted credentials (website, username, password) securely.

- AES-128 based encryption using Fernet
- Supports backup (encrypted JSON or binary format)
- Master key-based access and decryption
- Optionally integrates with environment variables for enhanced security

---

## How It Works

Each tool can be used independently, but together they form a secure password workflow:

1. **Generate** a strong password
2. **Analyze** its strength to ensure it’s secure
3. **Store** it safely using the password manager

---

## Getting Started

To run any project:

```bash
cd Project-Folder-Name
python filename.py