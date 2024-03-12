# Do the following challenges:
# Add letter G at the end of list.
# Replace letter in position 0 with letter Z.
# Remove letter C from list.
# Print list backwards.
# Ejemplo:

# Input: ["A", "B", "C", "D", "E", "F"]
# Output: ["G", "F", "E", "D", "B", "Z"]
letters = ['A', 'B', 'C', 'D', 'E', 'F']

# Adding letter G at the end
letters.append("G")
print(letters)

#Replace letter in position 0 with Z
letters.pop(0)
letters.insert(0, "Z")
# letters[0]="Z"
print(letters)

#Remove C from list
letters.remove("C")
print(letters)

letters.reverse()
print(letters)