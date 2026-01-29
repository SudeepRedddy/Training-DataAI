import time
from inputs import get_location, get_destination, get_user_details
from rides import show_rides, select_ride, start_ride
from bill import generate_bill

print("=" * 40)
print("Welcome to UBER".center(40))
print("=" * 40)

cities = {"Chennai", "Bangalore", "Mumbai", "Delhi", "Hyderabad"}

pickup = get_location(cities)
print("\nService available in:")
print("|| " + " || ".join(cities) + " ||\n")

destination = get_destination()
name, mobile = get_user_details()

show_rides()
ride = select_ride()
start_ride(ride)

distance = 12  
time.sleep(5)
print("\nYou have reached your destination:", destination)

generate_bill(name, mobile, pickup, destination, ride, distance)
