# A-Client-Server-Calculator
# TCP Arithmetic Server 🖥️➕➖✖️➗

A lightweight TCP server that handles basic arithmetic operations over network connections. Built with Python's `socket` library, this server listens for client requests, processes calculations, and returns results in real-time. Ideal for learning network programming fundamentals.

![Network Server Demo](https://img.shields.io/badge/Status-Stable-brightgreen) 
![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)

---

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Running the Server](#running-the-server)
  - [Connecting Clients](#connecting-clients)
- [Technical Design](#technical-design)
- [Error Handling](#error-handling)
- [Limitations](#limitations)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Features ✨
- **Basic Arithmetic Operations**: 
  - Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`)
- **Network-Ready**:
  - Listens on all interfaces (`0.0.0.0`) at port `54321`
  - Handles multiple sequential clients (one at a time)
- **Robust Error Handling**:
  - Invalid input formatting
  - Division by zero attempts
  - Unsupported operators
  - Connection drops
- **Clean Connection Management**:
  - Graceful shutdown with `over` command
  - Automatic socket cleanup

---

## Prerequisites 📋
- Python 3.7+
- Basic terminal/command prompt knowledge
- Network access to port `54321` (firewall configured if needed)

---

## Getting Started 🚀

### Running the Server
```bash
# Clone the repository
git clone https://github.com/your-username/tcp-arithmetic-server.git
cd tcp-arithmetic-server

# Start the server
python3 server.py

# Expected output:
# Socket successfully created.
# Server bound to 0.0.0.0:54321
# Server is listening for incoming connections...
