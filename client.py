import socket

def start_client(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            message = input("Enter message: ")
            s.sendall(message.encode())
            data = s.recv(1024).decode()
            print(f"Received: {data}")

if __name__ == "__main__":
    start_client()
