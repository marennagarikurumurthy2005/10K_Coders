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
list1=[10,5,8,6]
# a,b,c,d=list1 # var must be equal with number of elements in the list 
# print(a)

""" a,*b=list1 # * is used when var are less i.e when unpacking is targeted to created a list

print(a)
print(b) """

# List packing
# in simple merging 2 or more lists
list2=[8,6,7]
list3=[*list1,*list2] # * is a destructuring operator

print(list3)



