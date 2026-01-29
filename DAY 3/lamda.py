# add = lambda a,b,c : a + b - c
# print(add(2,3,-1))

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]
youngest_person = min(data, key=lambda x: x['age'] < 30)
print(youngest_person)
