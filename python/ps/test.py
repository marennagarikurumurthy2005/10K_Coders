
# Target Sum
# l1=[1,2,5,7,4,0]
# pairs=[]
# target=6
# for i in range(len(l1)):
#     # single=[]
#     for j in range(i+1,len(l1)):
#         if l1[i]+l1[j]==target:
#             # single.extend([l1[i],l1[j]])
#             pairs.append([l1[i],l1[j]])
#     # if len(single)>0:
#     #     pairs.append(single)
# print(pairs)


# rotate a string or list or anything
# right rotation
li=[1,2,3,4,5]
n=int(input("Enter number of rotations:"))
n=n%len(li)
print(li[-n:]+li[:-n])




