def print_header(title):
    print(title.center(40))

def show_customer_info(**kwargs):
    print_header("CUSTOMER DETAILS")
    for key, value in kwargs.items():
        if key.lower() == "phone":
            phone = str(value)
            masked_phone = phone[:2] + "XXXXXX" + phone[-2:]
            print(f"{key}: {masked_phone}")
        else:
            print(f"{key}: {value}")


def show_trip_details(**kwargs):
    print_header("TRIP DETAILS")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def calculate_total_bill(**kwargs):
    print_header("BILL SUMMARY")
    total = 0
    for key, value in kwargs.items():
        print(f"{key}: Rs {value}")
        total += value

    print("-" * 40)
    print(f"{'TOTAL AMOUNT'}: Rs {total}")
    print("=" * 40)
