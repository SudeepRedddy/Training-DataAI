print("Welcome to ZOMATO".center(40))
print("MENU".center(40))
print("1. Samosa  - Rs 20")
print("2. Coffee  - Rs 30")
print("3. Tea     - Rs 15")

SAMOSA_PRICE = 20
COFFEE_PRICE = 30
TEA_PRICE = 15

try:
    samosa = int(input("Enter number of Samosas: "))
    coffee = int(input("Enter number of Coffees: "))
    tea = int(input("Enter number of Teas: "))

    if samosa <= 0 and coffee <= 0 and tea <= 0:
        raise ValueError("At least one item quantity must be greater than zero")

    total = (
        samosa * SAMOSA_PRICE +
        coffee * COFFEE_PRICE +
        tea * TEA_PRICE
    )

except ValueError as ve:
    print("\nInvalid Input Error:", ve)

except TypeError:
    print("\nType Error: Please enter numeric values only")

except Exception as e:
    print("\n Unexpected Error:", e)

else:
    print("BILL SUMMARY".center(40))
    if samosa > 0:
        print(f"Samosa x {samosa} = Rs {samosa * SAMOSA_PRICE}")
    if coffee > 0:
        print(f"Coffee x {coffee} = Rs {coffee * COFFEE_PRICE}")
    if tea > 0:
        print(f"Tea    x {tea} = Rs {tea * TEA_PRICE}")

    print(f"{'TOTAL AMOUNT'}: Rs {total}")

finally:
    print("\nThank you for ordering from ZOMATO!")
    print(" Have a great day!")
