# file = open("notes.txt","w")
# file.write("Welcome to Python programming!")
# file.write("\nThis is a new line.")
# file.close()


# file = open("notes.txt","r")
# content = file.read()
# print(content)
# file.close()

# file = open("notes.txt","a")
# file.write("\nAppending a new line to the file.")
# file.close()

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

