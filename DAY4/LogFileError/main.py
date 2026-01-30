
errors = []

with open("error_logs.log","r") as log :
    for line in log :
        if "ERROR" in line :
            errors.append(line + "\n")
with open("error_out.txt","w") as err :
    for e in errors :
        err.write(e)
print("Completed")

