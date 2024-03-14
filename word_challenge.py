#Ask user to input a upperWord
# Make upperWord Uppercase
# Conditional ewordecution and continue to remove vocals from upperWord
# Print the rest of letters, each one in a separate line

word = input("Enter a word:")
upperWord = word.upper()
print("Upper:",upperWord)
print("Word:",word)

for letter in upperWord:
  if letter== "A" or letter=="E" or letter=="I" or letter=="O" or letter=="U":
    continue
  else:
    print(letter)