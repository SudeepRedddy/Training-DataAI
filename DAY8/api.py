import threading
import urllib.request
import json

def download_file():
    url="https://fakestoreapi.com/products/1"
    data=urllib.request.urlopen(url).read()
    posts=json.loads(data)
    
    with open("posts.json","w") as f:
        json.dump(posts,f,indent=4)

t1=threading.Thread(target=download_file)
t1.start()
print("Main thread continues to run while download is in progress.")