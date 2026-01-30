# feedback = input("Please provide your feedback about our service: ")
# with open("feedback.txt","w") as file :
#     file.write(feedback)
# print("Thankyou for your feedback")
# with open("data.txt", "r") as file :
#     print(file.readline().strip())
#     print(file.readline().strip())
#     print(file.readline().strip())

with open ("data.txt","r") as file :
    for i in range(3):
        line = file.readline()
        if not line : 
            break
        print(line.strip()) 