import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            # Receive message from server
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"\nServer: {message}")
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client.connect(('127.0.0.1', 5555))
    print("Connected to the server.")

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        msg = input()
        client.send(msg.encode('utf-8'))

if __name__ == "__main__":
    start_client()