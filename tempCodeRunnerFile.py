c0 = int(input("Enter a number: "))
steps = 0 
# loop repeat while c0 is different to 1
while c0 != 1:
  # if its even
  if c0 % 2 == 0:
    c0 = c0 / 2
    # print the number
    print(c0)
  else:
    c0 = 3 * c0 + 1
    # print the number
    print(c0)
  steps+=1

print("Steps: ", steps)