def generate_bill(name, mobile, pickup, drop, ride, distance):
    fare = distance * ride["rate"]
    file_name = f"bill_{name}.txt"

    with open(file_name, "w") as file:
        file.write("=" * 40 + "\n")
        file.write("UBER RIDE BILL\n".center(40))
        file.write("=" * 40 + "\n")
        file.write(f"Customer Name  : {name}\n")
        file.write(f"Mobile Number  : {mobile}\n")
        file.write(f"Pickup Location: {pickup}\n")
        file.write(f"Drop Location  : {drop}\n")
        file.write(f"Ride Type      : {ride['type']}\n")
        file.write(f"Driver Name    : {ride['driver']}\n")
        file.write(f"Distance       : {distance} km\n")
        file.write(f"Rate per km    : Rs. {ride['rate']}\n")
        file.write("-" * 40 + "\n")
        file.write(f"Total Fare     : Rs. {fare}\n")
        file.write("=" * 40 + "\n")
        file.write("Thank you for choosing UBER!\n")

    print(f"\nRide completed. Bill saved as '{file_name}'")
