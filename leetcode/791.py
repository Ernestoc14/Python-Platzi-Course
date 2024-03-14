# Custom Sort String

# You are given two strings order and s. All the characters of order are unique and were sorted in
# some custom order previously.
# Permute the characters of s so that they match the order that order was sorted. More specifically,
# if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

# Example 1:
# Input:  order = "cba", s = "abcd"
# Output:  "cbad"
# Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in order, it can be at any position in the returned string. "dcba",
# "cdba", "cbda" are also valid outputs.


# order = input("Enter the order: ")
# s = input("Enter the string: ")
def entries(order: str, s: str):
    orderSorted = sorted(order, s, reverse=False)
    return orderSorted


# Input:  order = "cba", s = "abcd"
# Output:  "cbad"
# s = "abcd"
order = "cba"
s = "abcd"

index = {char: index for index, char in enumerate(s)}
list_s = list(index.keys())
list_order = list(order)

for char in s:
  iterable = 0
  if char == list_s[1] and char == list_order[1]:
    print(char)
  else:
    print("No char")
  print(iterable)
