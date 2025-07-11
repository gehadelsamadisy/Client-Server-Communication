import socket

def handle_client(conn):
    while True:
        data = conn.recv(1024).decode() #1024 is the buffer size
        if not data:
            break
        print(f"Received: {data}")
        if data[0] == 'A':
            response = ''.join(sorted(data[1:], reverse=True))
        elif data[0] == 'C':
            response = ''.join(sorted(data[1:]))
        elif data[0] == 'D':
            response = data[1:].upper()
        else:
            response = data
        conn.sendall(response.encode())
    conn.close()

def start_server(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                handle_client(conn)

if __name__ == "__main__":
    start_server()
