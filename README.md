# CyberSecurity Toolkit
 [Thumbnail](./assets/thumbnail.jpg)

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

### 4. [SHA256](SHA256/)
A simple implementation of the SHA256 hashing algorithm using Python.

- SHA-256 is part of the Secure Hash Algorithm 2 family, designed for cryptographic security.
- It's a one-way function, meaning it's computationally infeasible to reverse the hashing process and retrieve the original input from the hash.
- SHA-256 is designed to be resistant to collision attacks, where different inputs produce the same hash value.
- It's widely used in various applications, including digital signatures, SSL/TLS certificates, and blockchain technology.
- SHA-256 can be used to verify the integrity of data, ensuring that the data hasn't been tampered with.

---

### 5. [LSB-Steganography](LSB-Steganography)
An implementation of LSB Steganography technique in Python.

- LSB steganography is a technique for hiding secret data within an image by manipulating the least significant bits (LSBs) of its pixels.
- The secret message is converted into a binary string (a series of 0s and 1s).
- The bits of the secret message are then embedded into the LSBs of the cover image's pixels. Each pixel's LSB is replaced with a bit from the message.
- To extract the hidden message, the receiver reads the LSBs of the modified image pixels and reconstructs the secret message. 

---

## Languages/Technologies Used

- Python 3
- SQL (MySQL/MariaDB)

---

## Getting Started

To run any project:

```bash
cd Project-Folder-Name
python filename.py
