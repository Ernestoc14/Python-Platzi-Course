#Create list
numbers = [1, 2, 3, 4, 5]
print("Create list: ", numbers)

#Read list
print("Reading list:", numbers[2])
print("Find a item in list by Index value: ", numbers.index(4))

#Update
numbers.append(0)
print("Updating list by adding a number at the end:", numbers)

numbers.insert(4, "Hello")
print("Updating list by insert value in position 4: ", numbers)

#Delete
numbers.pop(1)
print("Deleting number in List: ", numbers)
numbers.remove("Hello")
print("Remove item by value: ", numbers)