
# if the bill is above 1000 and its a weekend then the user is a gold memener then apply 20% discount

bill_amount = int(input("Enter the bill amount: "))
day = input("Enter the day (weekend/weekday): ").lower()
membership = input("Enter membership type (gold/silver/none): ").lower()    
if bill_amount > 1000 and day == "weekend" and membership == "gold":
    discount = bill_amount * 0.20
    final_amount = bill_amount - discount
    print(f"Discount applied: Rs {discount}. Final amount to be paid: Rs {final_amount}")
