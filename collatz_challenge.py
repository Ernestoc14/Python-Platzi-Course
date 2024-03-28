# 1 Take any non-negative and non-zero integer number and name it c0;
# 2 if it's even, evaluate a new c0 as c0 ÷ 2;
# 3 otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# 4 if c0 ≠ 1, go back to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.

# Write a program which reads one natural number and executes the above steps as long
# as c0 remains different from 1. We also want you to count the steps needed to achieve the goal. 
# Your code should output all the intermediate values of c0, too.

# Hint: the most important part of the problem is how to transform Collatz's idea into a while loop 
# this is the key to success.

# user gives a number
c0 = int(input("Enter a number: "))
steps = 0 
# loop repeat while c0 is different to 1
while c0 != 1:
  # if its even
  if c0 % 2 == 0:
    c0 /= 2
    # print the number
    print(c0)
  else:
    c0 = 3 * c0 + 1
    # print the number
    print(c0)
  steps+=1

print("Steps: ", steps)