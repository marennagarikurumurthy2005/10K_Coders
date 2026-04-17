
# how method overloading works in python? 


# list=[55,20,50,40,70]
# largest=list[0]
# second_largest=list[0]
# for i in list:
#     if i>largest:
#         second_largest=largest
#         largest=i
#     elif i>second_largest and i!=largest:
#         second_largest=i
# print(second_largest)


 


# list=[2,7,5,4,8]
# target=6
# new_list=[]
# l=len(list)
# for i in range(l):
#     for j in range(i,l):
#         if list[i]+list[j]==target:
#             new_list.extend([list[i],list[j]])
#             # new_list.append()

# print(new_list)




# def fun1(key):
#     print(key)

# def fun2(*args):
#     for i in args:
#         print(args)

# def fun3(**kwargs):
#     print(kwargs)

# def fun4(key=10,value):
#     print(key+value)


# fun1(10)
# fun2(10,20,30)
# fun3(name="Murthy",roll=24)
# fun4(key=20)


# class parent:
#     def set(self):
#         print("Im parent class")
# class child(parent):
#     def set(self):
#         print("Im child class")

# c=child()
# c.set()



# list[1,2,3,4,5,6,7]
# x=lambda x:list((list,x%2==0))

dici={"name":"MK","roll":24}
for i in dici:
    print(i,dici[i])


num=123
temp1=num
temp2=num
l=0
pro=0
while num>0:
    l+=1
    num//=10
while temp1>0:
    rem=temp1%10
    pro+=rem**l
    temp1//=10
if temp2==pro:
    print("armstrong")
else:
    print("not armstrong")



L=[2,4,6,8,10,1,5,3]
for i in L:
    if i%2==0:
        print(i)

A = [i for i in L if i%2==0]
