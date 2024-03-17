# Give it a list called my_list.
# Loop throught list to select just the positive numbers
# Then you have to add those numbers into a new list
# Show values in the new list

# Input: [1, -1, 2, -2, 3, -3, 4, -4]
# Output: [1, 2, 3, 4]
my_list = [1, -1, 2, -2, 3, -3, 4, -4]
positive = []
for num in my_list:
    if num > 0:
        positive.append(num)

print(positive)