import url.lib.request
import threading
import time

def download_file():
    url = "htpps://localhost:8000/jk.txt"
    filename = 'downloaded_test.txt'

    print("Starting download...")
    url.lib.request.urlretrieve(url, filename)
    print("Download completed.")
t = threading.Thread(target=download_file)
t.start()
print("Main Thread contineues...")
 