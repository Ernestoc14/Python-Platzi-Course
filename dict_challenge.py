# Your challenge is to do the following tasks:

# Add new element to dictionary with key of "twitter" and value "@nicobytes".
# Update value of element with key "name" and value "Felipe" 
# Delete element in dictionary with key "age"
# Print a list with all keys in dict
# Print a list with values in dict.
# Example:

# Input:
# person = {
#     "name": "Nicolas",
#     "lastName": "Molina",
#     "age": 29
# }

# Output:
# ["name", "lastName", "twitter"]
# ["Felipe", "Molina", "@nicobytes"]

person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}
# 1 - Add new element to dictionary with key of "twitter" and value "@nicobytes"
person["twitter"] = "@nicobytes"
# 2 - Update value of element with key "name" and value "Felipe" 
person['name'] = "Felipe"
# 3 - Delete element in dictionary with key "age"
del person['age']
# 4 - Print a list with all keys in dict
list_keys = list(person.items())
print(list_keys)
# 5 - Print a list with values in dict.
print(list(person.values()))
