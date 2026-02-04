import urllib.request
import json
import threading
import time
import sys

SERVER_URL = "http://127.0.0.1:8000"
username = ""
last_msg_count = 0

def receive_messages():
    global last_msg_count
    while True:
        try:
            with urllib.request.urlopen(f"{SERVER_URL}/messages") as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    if len(data) > last_msg_count:
                        for i in range(last_msg_count, len(data)):
                            msg = data[i]
                            if msg['user'] != username:
                                print(f"\n{msg['user']}: {msg['message']}")
                        last_msg_count = len(data)
        except Exception:
            pass
        time.sleep(1)

def send_message(message):
    data = json.dumps({'user': username, 'message': message}).encode('utf-8')
    req = urllib.request.Request(f"{SERVER_URL}/send", data=data, headers={'Content-Type': 'application/json'})
    try:
        urllib.request.urlopen(req)
    except Exception as e:
        print(f"Error sending message: {e}")

def start_client():
    global username
    username = input("Enter your username: ")
    
    threading.Thread(target=receive_messages, daemon=True).start()
    
    print("Connected! Type your messages below:")
    while True:
        msg = input()
        send_message(msg)

if __name__ == "__main__":
    start_client()