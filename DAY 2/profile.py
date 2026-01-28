def profile(**kwargs):
    list = []
    for key, value in kwargs.items():
        list.append(f"{key} : {value}")
    return list


name = input("Enter your name: ")
age =  int(input("Enter your age: "))
address = input("Enter your address: ")
blood_grp = input("Enter your blood group: ")

print(profile(Name=name, Age=age, Address=address, BloodGroup=blood_grp))