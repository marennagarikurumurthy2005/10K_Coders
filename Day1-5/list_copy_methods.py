""" # Shallow copy 

list1=[1,2,3,[2,5,8],4] # List 1
list2=list1.copy() # copying the list1 to second list 
print(list2)
# printing addresses
print("Original list address",id(list1))
print("copy list address",id(list2))
print("Inner list address")
print(id(list1[-2]))
print(id(list2[-1]))

list1.append(10)
print(list1)
print(list2)
list2.append(15)
print(list1)
print(list2)
# Inner list appending 
list2[-3].append(10)
print(list1)
print(list2)
 """

# Deep copy
# It dose not share the location of the both inner and outer lists 
# from copy import deepcopy

# list1=[1,2,3,[2,5,8],4]
# list2=deepcopy(list1)
# print(list1)
# print(list2)
# #Appending to list 1
# list1.append(10)
# print(list1)
# print(list2)
# print("Address of outerlists")
# print(id(list1[-2]))
# print(id(list2[-1]))


# List packing and unpacking
# list unpacking
# list1=[10,5,8,6]
# # a,b,c,d=list1 # var must be equal with number of elements in the list 
# # print(a)

# """ a,*b=list1 # * is used when var are less i.e when unpacking is targeted to created a list

# print(a)
# print(b) """

# # List packing
# # in simple merging 2 or more lists
# list2=[8,6,7]
# list3=[*list1,*list2] # * is a destructuring operator

# print(list3)
from copy import deepcopy

l1=[1,2,3,[4,5],6]
l2=l1.copy()
print("list 1 ",l1)
print("list2",l2)
# l2[-2].append(7)
# print("address of list 1",id(l1))
# print("address of list 2",id(l2))
# print()
# print("address of 1st outer list elements",id(l1[-1]))
# print("address of 2nd outer list elements",id(l2[-1]))
print()
# print("address of 1st inner list",id(l1[-2]))
# print("address of 2nd inner list ",id(l2[-2]))
print()
# print("address of l1 inner list elements",id(l1[-2][1]))
# print("address  of l2 inner list elements",id(l2[-2][1]))
print(l1)
print(l2)

print()
print()

l3=deepcopy(l1)
l3.append(10)
print("list 1 ",l1)
print("list3",l3)
print("list2",l3)

# print("address of list 1",id(l1))
# print("address of list 3",id(l3))
# print()
# print("address of 1st outer list",id(l1[-1]))
# print("address of 3st outer list",id(l3[-1]))
# print()
# print("address of inner list",id(l1[-2]))
# print("address of 3rd inner list ",id(l3[-2]))
# print()
# print("address of inner list elements",id(l1[-2][1]))
# print("address of inner list elements",id(l3[-2][1]))








