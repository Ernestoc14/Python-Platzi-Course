# reads a number of blocks and build a pyramid
# The pyramid is stacked according to one simple principle:
# each lower layer contains one block more than the layer above
# return the height of the pyramid
blocks = int(input("Enter the number of blocks: "))
blocksToBuild = 0
height= 0
iterable = 1
while blocks > 0:
  blocks -= blocksToBuild
  blocksToBuild += iterable
  if blocks > blocksToBuild:
    height +=1

print("The height of the pyramid: ", height)
