# class Emp:
#     def display(self,*args):
#         if len(args) == 2 :
#             print("2 Employess")
#         if len(args) == 1 :
#             print("1 Employee")

# e1 = Emp()
# e1.display(1)

class Employee : 
    def display(self, *args): 
        name,age,dept,empId,salary= args
        if(len(args) == 6 ):
            print("Employee Details : ")
            print(f"Employee Name : {name}")
            print(f"Employee Age : {age}")
            print(f"Employee Departement : {dept}")
            print(f"Employee ID : {empId}")
            print(f"Employee Salary : {salary}")
            # print(f"Employee Experience : {exp}")
        else :
            print("Enter all Employee Details")

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
dept = input("Enter Your Department: ")
empId = int(input("Enter Your Employee ID: "))
salary = int(input("Enter Your Salary: "))
# exp = int(input("Enter Your Experience: "))

e1 = Employee()
e1.display(name, age, dept, empId, salary)
