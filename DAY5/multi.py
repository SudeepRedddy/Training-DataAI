# class Device():
#     def display(self):
#         return "1080p"
#     def speaker(self):
#         return "sony"

# class laptop(Device):
#     def keybard(self):
#         return "Mech Keyboard"
    
# class Lenovo(laptop):
#     l1 = laptop()
#     print(l1.display())
#     print(l1.speaker())
#     print(l1.keybard())

# class Device():
#     def display(self):
#         return "1080p"
#     def speaker(self):
#         return "sony"

# class laptop():
#     def keyboard(self):
#         return "Mech"
        
# class mobile(Device,laptop):
#     def keyboard1(self):
#         return "touch"
    
# m1 = mobile()
# print(m1.display())
# print(m1.speaker())
# print(m1.keyboard())
# print(m1.keyboard1())

class A:
    # def display(self):
    #     print("Display from class A")
    def display(self):
        print("Hello")

class B:
    def display(self):
        print("Display from class B")

class C(A, B):
    def display(self):
        super(A,self).display()

c = C()
c.display()

