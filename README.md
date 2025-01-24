# A-Client-Server-Calculator
# TCP Arithmetic Server 🖥️➕➖✖️➗

A lightweight TCP server that handles basic arithmetic operations over network connections. Built with Python's `socket` library, this server listens for client requests, processes calculations, and returns results in real-time. Ideal for learning network programming fundamentals.

![Network Server Demo](https://img.shields.io/badge/Status-Stable-brightgreen) 
![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)

---

# Simple Calculator Client-Server Application

This project implements a basic **client-server application** for performing simple arithmetic operations using Python's `socket` module. The server performs the calculations, and the client sends requests to the server.

## Features
- **Server**: Handles multiple arithmetic operations such as addition, subtraction, multiplication, and division.
- **Client**: Sends operation requests to the server and receives the results.
- Error handling for invalid input, unsupported operations, and division by zero.
- Graceful connection termination with the keyword `Over`.

---

## How It Works
1. **Server**:
   - Listens for incoming connections on a specified IP address and port.
   - Processes operations sent by the client.
   - Sends the results or error messages back to the client.

2. **Client**:
   - Connects to the server using its IP address and port.
   - Sends operations in the format: `operand operator operand` (e.g., `4 + 5`).
   - Receives the result from the server and displays it.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**: 
  - `socket`: For network communication.

---

## Prerequisites
Ensure you have Python 3 installed on your system.

## Example Usage

### Server
```bash
Socket successfully created.
Server bound to 127.0.0.1:54321
Server is listening for incoming connections...
Server started
Waiting for client request..
Connected client : ('127.0.0.1', 12345)
Received operation: 4 + 5
```
### Client
```bash
Example: 4 + 5
Enter the operation in the form operand operator operand: 4 + 5
Answer is 9.0
Type 'Over' to terminate
```

