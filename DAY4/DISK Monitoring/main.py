import shutil

storage = shutil.disk_usage('/')
total = storage.total
used = storage.used
free = storage.free

bytes = 1024**3

print("Total Storage", total / bytes)
print("Used Storage", used / bytes)
print("Free Storage", free / bytes)

