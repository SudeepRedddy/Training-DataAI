# Hello World
# print("Hello, World!")

# add two numbers
# def add(a,b):
#     return a + b
# print(add(5,7))

# Factorial of a number
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n - 1)
# print(fact(5))

# Power of a number
# def pow(a,b):
#     if b == 0:
#         return 1
#     return a * pow(a, b - 1)
# print(pow(2,5))

# Check if a number is prime
# def isPrime(num, div):
#     if num < 2:
#         return False
#     if div == 1:
#         return True
#     if num % div == 0:
#         return False
#     return isPrime(num, div - 1)
# print(isPrime(29, 28))

# Simple Calculator
# def calci(n,m,ope):
#     if(ope == '+'):
#         return n + m
#     elif(ope == '-'):
#         return n - m
#     elif(ope == '*'):
#         return n * m
#     elif(ope == '/'):
#         return n / m
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# op = input("Enter operation: ")
# print(calci(a,b,op))    

# python intro
# setting up pytho
# syntax data types
# functions recursion
# project

# Form Validator

# def formValidator(email,password,name,age):
#     if "@" not in email:
#         return "Invalid email"
#     if len(password) < 6:
#         return "Incorrect password Length"
#     if len(name) == 0:
#         return "Name cannot be empty"
#     if not age.isdigit():
#         return "Age must be a number"
#     return "Valid Form"

# email = input("Enter your email: ")
# password = input("Enter your password: ")
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(formValidator(email,password,name,age))

#Scripting

# import sys
# print("Prog Name: ", sys.argv[0])
# for i in range(1, len(sys.argv)):
#     print("Argument ", i, ": ", sys.argv[i])

# import sys
# if len(sys.argv) > 2:
#     print("Arguments: ", sys.argv)
# else:
#     print("provide more arguments")

# import shutil
# import datetime

# source = "C:/Users/sudee/Downloads/Capgemini/Python/data.txt"
# destination = f"C:/Users/sudee/Downloads/Capgemini/Python/data_backup_{datetime.date.today()}.txt"
# shutil.copy(source, destination)
# print(f"Backup of {source} created successfully at {destination}.")


# import os
# import shutil

# source_folder = "C:/Users/sudee/Downloads/Capgemini/Python"

# jpeg_backup_folder = os.path.join(source_folder, "JPEG backup")
# os.makedirs(jpeg_backup_folder, exist_ok=True)
# for file in os.listdir(source_folder):
#     if file.lower().endswith((".jpg", ".jpeg")):
#         source_path = os.path.join(source_folder, file)
#         destination_path = os.path.join(jpeg_backup_folder, file)
#         shutil.copy(source_path, destination_path)
#         print(f"Copied: {file}")
# print("All JPEG images have been copied successfully.")
