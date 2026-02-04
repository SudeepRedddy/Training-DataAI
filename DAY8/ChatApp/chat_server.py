import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\nClient: {message}")
        except:
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.bind(('127.0.0.1', 5555))
    
    server.listen(1)
    print("Server started. Waiting for connection on port 5555...")

    client_socket, addr = server.accept()
    print(f"Connection established with {addr}")

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        msg = input()
        client_socket.send(msg.encode('utf-8'))

if __name__ == "__main__":
    start_server()