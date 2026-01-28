
attendance = int(input("Enter the attendance percentage: "))
marks = int(input("Enter the marks obtained: "))
if attendance >= 75 and marks >= 50:
    print("Eligible to sit for the exam")
else:
    print("Not eligible to sit for the exam")

recharge_amount = int(input("Enter the recharge amount: "))
data_balance = int(input("Enter the current data balance in GB: "))
if recharge_amount >= 300 or data_balance >= 2:
    print("You are eligible for a additonal 1GB data bonus")