import time

RIDES = {
    "1": {"type": "Sedan", "driver": "Ravi", "rate": 15},
    "2": {"type": "Hatchback", "driver": "Amit", "rate": 10},
    "3": {"type": "SUV", "driver": "Suresh", "rate": 20}
}


def show_rides():
    print("\nChoose the type of ride:")
    print("1. Sedan       (Rs. 15/km)")
    print("2. Hatchback   (Rs. 10/km)")
    print("3. SUV         (Rs. 20/km)")


def select_ride():
    choice = input("Enter your choice (1/2/3): ")
    if choice not in RIDES:
        print("Invalid ride choice!")
        exit()
    return RIDES[choice]


def start_ride(ride):
    print("\nFinding UBER rides near your location...")
    time.sleep(2)
    print(f"Your ride choice : {ride['type']}")
    print(f"Driver assigned  : {ride['driver']}")
    print("Your ride will arrive in 5 minutes...")
    time.sleep(2)
    print("\nYour ride has arrived")
