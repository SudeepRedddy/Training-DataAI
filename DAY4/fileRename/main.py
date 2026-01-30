import os

old_name = "hello.txt"
new_name = "Changed.txt"

os.rename(old_name,new_name)
print("Name Changed Succesfully")