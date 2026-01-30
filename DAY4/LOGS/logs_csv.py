ip_address = []
with open("sample_logs.log","r") as log :
    lines = log.readlines()

    for line in lines :
        words = line.split("[")
        # print(words)
        ip_addr = words[1].split("]")
        ip_address.append(ip_addr[0])

with open("ip_addr_out.csv","w") as ip:
    for ip_add in ip_address :
        ip.write(ip_add + ",")

print("Completed")
