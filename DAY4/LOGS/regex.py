import re
error = []
with open("sample_logs.log","r") as log :
    for line in log:
        if re.search("login HTTP",line):
            error.append(line)
        
with open("error.txt","w") as f:
    for ip_add in error :
        f.write(ip_add + "\n")

print("Completed")
