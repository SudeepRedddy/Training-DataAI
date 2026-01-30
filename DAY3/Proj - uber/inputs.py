def get_location(cities):
    location = input("Enter your current location: ").title()
    if location not in cities:
        print("Sorry, our service is not available at your location.")
        exit()
    return location


def get_destination():
    return input("Enter your destination: ").title()


def get_user_details():
    name = input("Enter your name: ").title()
    mobile = input("Enter your mobile number: ")

    if len(mobile) != 10 or not mobile.isdigit():
        print("Invalid mobile number!")
        exit()

    return name, mobile
