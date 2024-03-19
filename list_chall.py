# write a line of code to ask the user to replace the center element in the list
# write a line of code to delete the last element on list
# write a line of code to print the lenght of the list

list = [1, 2, 3, 4, 5]
center_index = len(list) // 2
new_element = int(input("Replace enter element for a new one: "))
list[center_index] = new_element
del list[-1]
print("Last item deleted: ", list)
print("List Lenght: ", len(list))
