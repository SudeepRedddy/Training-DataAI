import re
import string

def check_password_strength(password):
    length_ok = len(password) >= 8
    upper_ok = re.search(r'[A-Z]', password)
    lower_ok = re.search(r'[a-z]', password)
    digit_ok = re.search(r'\d', password)
    special_ok = re.search(rf'[{re.escape(string.punctuation)}]', password)

    if all([length_ok, upper_ok, lower_ok, digit_ok, special_ok]):
        return "Strong Password"
    else:
        return "Weak Password"


password = input("Enter password: ")
print(check_password_strength(password))
