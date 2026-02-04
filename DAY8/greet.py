import threading

def greet(name):
    print(f"Hello, {name}")

t = threading.Thread(target=greet, args=("Sudeep",))
t.start()
