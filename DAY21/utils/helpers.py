# Placeholder for common utility functions like password hashing, validation helpers, etc.
from werkzeug.security import generate_password_hash, check_password_hash
import re

def hash_password(password):
    return generate_password_hash(password)

def check_hashed_password(hashed_password, password):
    return check_password_hash(hashed_password, password)

def is_valid_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email) is not None

def is_valid_password_length(password, min_length=8):
    return len(password) >= min_length