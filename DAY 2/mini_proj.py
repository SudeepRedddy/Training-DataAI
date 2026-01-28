# show customer info total bill value

def get_name(**kwargs):
    for key, value in kwargs.items():
        if key == "Phone":
            phone = str(value)[:2] + "XXXXXX" + str(value)[-2:]
            print(f"{key}: {phone}")
        else:
            print(f"{key}: {value}")

def trip_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def calculate_total_bill(**kwargs):
    total = 0
    for key, value in kwargs.items():
        print(f"{key}: Rs {value}")
        total += value
    print(f"Total Bill Amount: Rs {total}")

print("-------------------------")
get_name(Name="Sudeep", Phone=9876543210, Email="sudeep@gmail.com")

print("-------------------------")
trip_details(Trip="Shimla", Days=5, Budget=25000)

print("-------------------------")
calculate_total_bill(Transport=10000, Food=5000, Accommodation=7000)
print("-------------------------")
print("-------------------------")
calculate_total_bill(Clothes=10000, Food=5000, Taxi=7000)
