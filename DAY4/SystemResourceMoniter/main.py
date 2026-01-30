import psutil

ram = psutil.virtual_memory()
storage = psutil.disk_usage('/')

print("Storage Available : ",storage.total / 1024 ** 3)
print("Storage Free      : ",storage.free / 1024 ** 3)
print("Storage Used      : ",storage.used / 1024 ** 3)
print("Ram Available     : ",ram.total / 1024 ** 3)
print("Ram Free          : ",ram.free / 1024 ** 3)
print("Ram Used          : ",ram.used / 1024 ** 3)
