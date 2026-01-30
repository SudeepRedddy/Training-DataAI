import input
import logic


def main():
    customer = input.get_customer_input()
    logic.show_customer_info(**customer)

    trip = input.get_trip_input()
    logic.show_trip_details(**trip)
    bill = input.get_bill_input()
    logic.calculate_total_bill(**bill)


if __name__ == "__main__":
    main()
