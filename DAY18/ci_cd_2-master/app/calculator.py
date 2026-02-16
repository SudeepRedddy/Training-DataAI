import requests

def add(a, b):
    return a + b+0

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def get_api_status():
    try:
        response = requests.get("https://api.github.com")
        return response.status_code
    except Exception:
        return 500
