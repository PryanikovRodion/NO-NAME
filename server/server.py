import socket
import threading
from config import PORT, MAX_CONNECTIONS
from handlers import handle_request

def client_handler(conn):
    with conn:
        data = conn.recv(1024).decode()
        response = handle_request(data)
        conn.sendall(response.encode())

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(MAX_CONNECTIONS)

    print(f"Сервер запущен на порту {PORT}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Новое подключение: {addr}")
        thread = threading.Thread(target=client_handler, args=(conn,))
        thread.start()

if __name__ == "__main__":
    start_server()
