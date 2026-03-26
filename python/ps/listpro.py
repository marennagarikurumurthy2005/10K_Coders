# # add element to a list 
# list=[1,2,3,2,5,2,7,2]
# def add_element(num):
#     list.append(num)
#     return list
# a=add_element(4)
# print(a)


# # remove element in the list 
# def remove_element(num):
#     if num in list:
#         list.remove(num)
#     return list
# b=remove_element(4)
# print(b)


# # find maximum number in a list
# maxim=list[0]
# for i in list:
#     if i >maxim:
#         maxim=i
# print(maxim)


# #count occurence of 
# def count(value):
#     count=0
#     for i in list:
#         if i==value:
#             count+=1
#     return count
# num=2
# d=count(num)
# print(num,d)

# # reverse a list
# print(list[len(list)::-1])

# # sorting a list
# list=[1,6,2,8,7,3]
# l=len(list)
# for i in range(l):
#     for j in range(i,l):
#         if list[i]>list[j]:
#             list[i],list[j]=list[j],list[i]
# print(list)

# remove duplicates
# list=[1,2,4,5,2,6,1,7,5]
# print(set(list))

# new_list=[]
# match=list[0]
# for i in list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

        
          


# merging 2 lists
# l1=[1,2]
# l2=[3,4,2]
# l3=l1+l2 
# print(l3)

# # common elements in 2 list:
# for i in l1:
#     if i in l2:
#         print(i)




# find second largest element in a list 
# finding second smallest number in list
# copy list to another list
# printing prime numbers in a list 
# replace all zeros with given number in a list
# check all numbers are same or not in a list 



# list=[10,5,8,60]
# largaest=list[0]
# second_largest=list[0]
# for i in list:
#     if i>largaest:
#         second_largest=largaest
#         largaest=i
#     elif second_largest<i and i!=largaest:
#         second_largest=i
# print(second_largest)

# finding second smallest number 
# list=[10,5,8,60]
# smallest=list[0]
# second_smallest=list[0]
# for i in list:
#     if i<smallest:
#         second_smallest=smallest
#         smallest=i
#     elif second_smallest>i and i!=smallest:
#         second_smallest=i
# print(second_smallest)


# copy list to another list

# l1=[1,3,5,7]
# # l2=l1.copy()
# l2=l1[::]
# print(l2)

# printing prime numbers in a list 
# list=[1,2,3,4,5,8,10,11,12,13,14,17]
# for i in list:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

# replace all zeros with given number
# list=[0,2,5,7,6,3,0]
# given_num=-1
# for i in range(len(list)):
#     if list[i]==0:
#         list[i]=given_num
# print(list)

# check all numbers are same or not 

# same=True
# list=[5,5,5,5]
# for i in list:
#     if i!=list[0]:
#         same=False
#         break
# if same:
#     print("Same elements in list")
# else:
#     print("non same elements")


