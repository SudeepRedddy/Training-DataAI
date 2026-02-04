import time 
import threading
import urllib.request
import json
import ssl

def download_file():
  try:
    print("connecting to API...")
    time.sleep(2)
    url='https://fakestoreapi.com/products'
    header={
       "user-Agent":"Mozilla/5.0"
    }
    res=urllib.request.Request(url,headers=header)
    context=ssl._create_unverified_context()
    with urllib.request.urlopen(res,context=context) as response:
      data=response.read()
    print("Download completed")

    posts=json.loads(data)
    with open("products.json","w") as f:
        json.dump(posts,f,indent=4)
    print("Data saved to products.json")
  except Exception as e:
        print("An error occurred:",e)
t=threading.Thread(target=download_file)
t.start()
print("Main thread continues execution...")