import threading
import time
def worker(num):
    print(f"Worker {num} is running")
    time.sleep(1)
    print(f"Worker {num} has finished")

for i in range(5):
    t = threading.Thread(target=worker,args=(i,))
    t.start()