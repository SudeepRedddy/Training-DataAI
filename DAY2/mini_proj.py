def print_header(title):
    print("\n" + "=" * 40)
    print(f"{title.center(40)}")
    print("=" * 40)


def show_customer_info(**kwargs):
    print_header("CUSTOMER DETAILS")
    for key, value in kwargs.items():
        if key.lower() == "phone":
            phone = str(value)
            masked_phone = phone[:2] + "XXXXXX" + phone[-2:]
            print(f"{key:<10}: {masked_phone}")
        else:
            print(f"{key:<10}: {value}")

def show_trip_details(**kwargs):
    print_header("TRIP DETAILS")
    for key, value in kwargs.items():
        print(f"{key:<15}: {value}")

def calculate_total_bill(**kwargs):
    print_header("BILL SUMMARY")
    total = 0
    for key, value in kwargs.items():
        print(f"{key:<15}: Rs {value}")
        total += value

    print("-" * 40)
    print(f"{'TOTAL AMOUNT':<15}: Rs {total}")
    print("=" * 40)


name = input("Enter your name          : ")
phone = input("Enter your phone number  : ")
email = input("Enter your email         : ")

show_customer_info(Name=name, Phone=phone, Email=email)

trip = input("\nEnter your trip destination : ")
days = int(input("Enter number of days        : "))
budget = int(input("Enter your budget           : "))

show_trip_details(Trip=trip, Days=days, Budget=f"Rs {budget}")

calculate_total_bill(
    Transport=10000,
    Food=5000,
    Accommodation=7000
)
