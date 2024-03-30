# Given a list of nums [1,2,4,-5,7,9,3,2]
# create another list that contains all items in sorted order
# from min to max
# Output: [-5,1,2,2,3,7,9]

L = [1,2,4,-5,7,9,3,2]

for index in range(len(L)):
    min_index = index
    for num in range(index+1, len(L)):
        if L[num] < L[min_index]:
            min_index = num
    L[index], L[min_index] = L[min_index], L[index]

print(L)
# for index in range(len(L)):
#   first_num = L[index]
#   idx = index
#   iterator = index
#   #number in List
#   for num in range(len(L)):
#     if L[num] < first_num:
#       first_num = L[num]
#       idx = iterator
#     iterator+=1
#   temporal = L[index]
#   L[index] = L[idx]
#   L[idx] = temporal
# print(L, index)
# for num in L:
#     if num < first_num:
#         L[index] = num

#     index += 1
#     first_num=L[index]

# print(L)
