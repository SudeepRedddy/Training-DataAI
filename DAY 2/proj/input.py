def get_customer_input():
    name = input("Enter your name          : ")
    phone = input("Enter your phone number  : ")
    email = input("Enter your email         : ")

    return {
        "Name": name,
        "Phone": phone,
        "Email": email
    }


def get_trip_input():
    trip = input("\nEnter your trip destination : ")
    days = int(input("Enter number of days        : "))
    budget = int(input("Enter your budget           : "))

    return {
        "Trip": trip,
        "Days": days,
        "Budget": f"Rs {budget}"
    }


def get_bill_input():
    print("\nEnter Expense Details")
    transport = int(input("Transport Cost        : Rs "))
    food = int(input("Food Cost             : Rs "))
    accommodation = int(input("Accommodation Cost    : Rs "))

    return {
        "Transport": transport,
        "Food": food,
        "Accommodation": accommodation
    }
