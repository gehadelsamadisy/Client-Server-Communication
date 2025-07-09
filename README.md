# Client-Server Communication System

## Project Overview

This project implements a robust client-server communication system using Python's socket programming. The system demonstrates fundamental networking concepts including TCP socket communication, data processing, and multi-client handling. The server processes incoming messages based on specific protocols and returns processed results to clients.

## Features

### Core Functionality

- **TCP Socket Communication**: Implements reliable TCP-based client-server communication
- **Multi-Client Support**: Server can handle multiple client connections sequentially
- **Message Processing**: Server processes messages according to specific protocols:
  - **Protocol A**: Sorts characters in descending order (excluding first character)
  - **Protocol C**: Sorts characters in ascending order (excluding first character)
  - **Protocol D**: Converts text to uppercase (excluding first character)
  - **Default**: Echoes back the original message

### Technical Features

- **Connection Management**: Proper socket lifecycle management with context managers
- **Error Handling**: Graceful handling of connection termination
- **Configurable Network Parameters**: Customizable host and port settings
- **Real-time Communication**: Interactive message exchange between client and server

## Installation

### Prerequisites

- Python 3.6 or higher
- No additional dependencies required (uses only Python standard library)

### Setup Instructions

1. Clone or download the project files
2. Ensure both `client.py` and `server.py` are in the same directory
3. No additional installation steps required

## Usage

### Starting the Server

```bash
python server.py
```

The server will start listening on `127.0.0.1:12345` by default.

### Starting the Client

```bash
python client.py
```

The client will attempt to connect to the server at `127.0.0.1:12345`.

### Communication Protocol

#### Message Format

- **Protocol A**: `A<message>` - Server sorts characters in descending order
- **Protocol C**: `C<message>` - Server sorts characters in ascending order
- **Protocol D**: `D<message>` - Server converts to uppercase
- **Default**: `<message>` - Server echoes back the original message

#### Example Interactions

**Protocol A (Descending Sort):**

```
Client: Ahello
Server: ollhe
```

**Protocol C (Ascending Sort):**

```
Client: Cworld
Server: dlorw
```

**Protocol D (Uppercase):**

```
Client: Dpython
Server: PYTHON
```

**Default (Echo):**

```
Client: Hello World
Server: Hello World
```

## Configuration

### Server Configuration

The server can be configured by modifying the parameters in `server.py`:

```python
def start_server(host='127.0.0.1', port=12345):
```

### Client Configuration

The client can be configured by modifying the parameters in `client.py`:

```python
def start_client(host='127.0.0.1', port=12345):
```

## Technical Implementation Details

### Server Architecture

- **Socket Creation**: Uses `socket.AF_INET` for IPv4 and `socket.SOCK_STREAM` for TCP
- **Binding**: Binds to specified host and port
- **Listening**: Accepts incoming connections
- **Client Handling**: Processes each client in a dedicated connection loop
- **Message Processing**: Implements protocol-based message transformation

### Client Architecture

- **Connection Establishment**: Connects to server using TCP socket
- **Interactive Communication**: Provides user interface for message input
- **Message Exchange**: Sends messages and receives responses
- **Continuous Operation**: Maintains connection until user termination

### Network Protocol Details

- **Transport Protocol**: TCP (Transmission Control Protocol)
- **Address Family**: IPv4
- **Buffer Size**: 1024 bytes for message reception
- **Encoding**: UTF-8 for message encoding/decoding

## Testing

### Manual Testing Steps

1. Start the server: `python server.py`
2. Start the client: `python client.py`
3. Enter test messages with different protocols:
   - `Ahello` → Should return `ollhe`
   - `Cworld` → Should return `dlorw`
   - `Dpython` → Should return `PYTHON`
   - `Hello` → Should return `Hello`

### Expected Behavior

- Server displays connection information and received messages
- Client displays server responses
- Connection remains active until client termination
- Server continues listening for new connections

## Performance Characteristics

- **Latency**: Minimal latency for local network communication
- **Throughput**: Limited by network bandwidth and processing speed
- **Scalability**: Sequential client handling (not concurrent)
- **Reliability**: TCP ensures reliable message delivery

## Security Considerations

- **Local Network**: Currently configured for localhost only
- **No Authentication**: No client authentication implemented
- **No Encryption**: Messages transmitted in plain text
- **Buffer Overflow Protection**: Limited by 1024-byte buffer size

## Limitations and Future Enhancements

### Current Limitations

- Single-threaded server (handles one client at a time)
- No persistent connection management
- Limited error handling for network issues
- No logging or monitoring capabilities

### Potential Enhancements

- **Multi-threading**: Support for concurrent client connections
- **Connection Pooling**: Efficient connection management
- **Enhanced Protocols**: Additional message processing protocols
- **Logging**: Comprehensive logging and monitoring
- **Configuration Files**: External configuration management
- **Security**: SSL/TLS encryption and authentication

## Learning Objectives

This project demonstrates:

- **Socket Programming**: Understanding of TCP socket communication
- **Client-Server Architecture**: Implementation of client-server model
- **Protocol Design**: Custom message processing protocols
- **Network Programming**: Practical experience with network communication
- **Python Networking**: Usage of Python's socket library

## 🤝 Contributing

This is an academic project for Computer Networks. For educational purposes, feel free to:

- Study the code implementation
- Experiment with different protocols
- Extend functionality for learning purposes
- Provide feedback on code structure and design
