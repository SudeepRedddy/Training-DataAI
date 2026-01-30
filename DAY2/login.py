full_name = "Sudeep Reddy"
initials = "".join(full_name.split(" ")[0][0] + full_name.split(" ")[1][0])
print(initials)

user_name = input("Enter the user_name: ")
password = input("Enter the password: ")

if user_name == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")
