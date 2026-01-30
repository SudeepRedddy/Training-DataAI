import string

def check_password_strength(password):
    length_ok = len(password) >= 8
    upper_ok = any(c.isupper() for c in password)
    lower_ok = any(c.islower() for c in password)
    digit_ok = any(c.isdigit() for c in password)
    special_ok = any(c in string.punctuation for c in password)

    if all([length_ok, upper_ok, lower_ok, digit_ok, special_ok]):
        return "Strong Password"
    else:
        return "Weak Password"


password = input("Enter password: ")
print(check_password_strength(password))
