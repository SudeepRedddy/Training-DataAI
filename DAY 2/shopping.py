list = []
while True:
    item = input("Enter the item: ")
    if item == "done":
        break
    list.append(item)
print("Items in the cart:")
print(list)