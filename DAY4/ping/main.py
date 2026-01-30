import subprocess

servers = ["8.8.8.8","8.8.8.4","google.com","facebok.com"]

for server in servers :
    print("Pinging Server: ",server)
    res = subprocess.run(["ping","-n","1",server],stdout = subprocess.DEVNULL,stderr = subprocess.DEVNULL)

    if res.returncode == 0 :
        print(f"{server} is running")
    else :
        print(f"{server} is Down")

print("completed")