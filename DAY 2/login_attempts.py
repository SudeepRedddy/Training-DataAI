user_name = input("Enter the user_name: ")
password = input("Enter the password: ")
no_of_attempts = 3
while no_of_attempts > 0:
    if user_name == "admin" and password == "1234":
        print("Login Successful")
        break
    else:
        no_of_attempts -= 1
        print(f"Invalid Credentials. You have {no_of_attempts} attempts left.")
        if no_of_attempts == 0:
            print("Account locked due to multiple failed login attempts.")
        else:
            user_name = input("Enter the user_name: ")
            password = input("Enter the password: ")

            


