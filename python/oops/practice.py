# #  class , objects , inheritance--> aquiring properties of parent class

# # class parent:
# #     def __init__(self,num1,num2):
# #         self.num1=num1
# #         self.num2=num2
# #     def details(self):
# #         print(self.num1)
# #         print(self.num2)
# # class child(parent):
# #     def __init__(self, num1, num2,num3):
# #         super().__init__(num1, num2,)
# #         # self.num1=num1
# #         # self.num2=num2
# #         self.num3=num3
# #     def getdata(self):
# #         super().details()
# #         print(self.num3)

# # ch=child(10,20,30)
# # ch.getdata()

# # multi-level inheritance

# # class thatha:
# #     def __init__(self,age):
# #         self.age=age
# #     def detail1(self):
# #         print("Thatha age:",self.age)

# # class nanna(thatha):
# #     def __init__(self, age):
# #         super().__init__(age)
# #     def detail2(self):
# #         super().detail1()
# #         self.age=self.age-20
# #         print("Nanna age:",self.age)
# # class child(nanna):
# #     def __init__(self, age):
# #         super().__init__(age)
# #     def detail3(self):
# #         super().detail2()
# #         self.age=self.age-20
# #         print("child age:",self.age)

# # obj=child(60)
# # obj.detail3()


# #  multiple , heirarical , hybrid
  
# # abstraction hides implementation and provides structure of the methods using abstract method 

# # from abc import ABC, abstractmethod

# # class payment(ABC):
# #     @abstractmethod
# #     def pay(self,amount):
# #         pass
# # class upi(payment):
# #     def pay(self,amount):
# #         print(amount)
# # class check(payment):
# #     def pay(self,amount):
# #         print(amount)
# # class netbank(payment):
# #     def pay(self, amount):
# #         print(amount)

# # class user():
# #     def userselection(self,mode,amount):
# #         mode.pay(amount)
    
# # t1=upi()
# # t2=check()
# # t3=netbank()
# # obj=user()
# # obj.userselection(t1,180)



# # encapsulation: wrapping data and implementation together also provides security 
# # if x is a variale then self.x is public self._x protected self.__x is provate 
# #  for protected and private  we can only access that too with function calls but not directly with variable name it but cannot be modified

# # from abc import abstractmethod,ABC

# # class payment(ABC):
# #     @abstractmethod
# #     def credit(self,amount):
# #         pass
# #     @abstractmethod
# #     def debit(self,amount):
# #         pass
# #     @abstractmethod
# #     def available(self):
# #         pass

# # class upi(payment):
# #     def __init__(self,initial):
# #         self.__initial=initial
        
# #     def credit(self, amount):
# #         print(self.__initial+amount)
# #     def debit(self, amount):
# #         if amount<self.__initial:
# #             print(self.__initial-amount)
# #         else:
# #             print("insufficient")
# #     def available(self):
# #         print(self.__initial)

# # obj=upi(1000)
# # # obj.credit(100)
# # # obj.debit(1500)
# # # obj.debit(300)
# # obj.available()


# # polymorphism same method name but different behavious 

# # from abc import abstractmethod,ABC

# # class animal(ABC):
# #     @abstractmethod
# #     def sound(self,made):
# #         pass
# # class dog(animal):
# #     def sound(self, made):
# #         print(made)
# # class cat(animal):
# #     def sound(self, made):
# #         print(made)

# # obj=dog()
# # obj.sound("bark")

# # obj=cat()
# # obj.sound("meow")


# #  crud operations

# from abc import ABC,abstractmethod

# class student(ABC):
#     @abstractmethod
#     def add_details(self,items):
#         pass

#     @abstractmethod
#     def update_details(self,roll,**kwargs):
#         pass

#     @abstractmethod
#     def delete_details(self,roll):
#         pass

#     @abstractmethod
#     def view_details(self):
#         pass


# class ds:
#     def __init__(self,name,roll,course):
#         self.name=name
#         self.roll=roll
#         self.course=course
# class ds_management(student):
#     details=[]
#     def add_details(self, items):
#         self.details.append(items)
#         print("details added")

#     def update_details(self, roll, **kwargs):
#         for s in self.details:
#             if roll==s.roll:
#                     if "newroll" in kwargs:
#                         s.roll=kwargs["newroll"]
#                     if "name" in kwargs:
#                         s.name=kwargs["name"]
#                     if "course" in kwargs:
#                         s.course=kwargs["course"]
#                     return
#         else:
#             print("roll number not exist")
                
#     def delete_details(self, roll):
#         for s in self.details:
#             if s.roll==roll:
#                 self.details.remove(s)
#                 print("deleted successfully")
#                 return
#             else:
#                 print("roll not found")
#     def view_details(self):
#         for i in self.details:
#             print(i.name,end=" ")
#             print(i.roll,end=" ")
#             print(i.course)


# ds_obj1=ds("Murthy",24,"DS")
# ds_obj2=ds("Murugan",25,"DS")

# dsm_obj=ds_management()

# dsm_obj.add_details(ds_obj1)
# dsm_obj.add_details(ds_obj2)

# dsm_obj.view_details()

# dsm_obj.delete_details(25)

# dsm_obj.view_details()

# dsm_obj.update_details(roll=24,name="Kurumurthy")
# dsm_obj.view_details()






    
    
        
        
    

    
    
    

        
        





# # class questions:
# #     q1="find the min distance of the fib number to the sum of array"
# #     hint="a<sum<b ; a,b are fib numbers"
# #     q2="find the time difference of give time interval"
# #     input="10:10am-10:30pm"
# #     q3="find the list is in arithmetic or geometric sequence else print -1"
# #     hint="ap distance between numbers is same , gp ratio of numbers is same"
# #     q4="insert * between even numbers - between odd numbers do not consider 0 as even"
# #     example="254809763 to 254*809-763"

    



    
# inp="abc"
# arr=[]
# for y in range(len(inp)):
#     for i in range(len(inp)-1):
#         j=0
#         k=0
#         x=inp[y]
#         while(j<len(inp)):
#             if j>=len(inp):
#                 j=0
#             else:
#                 j=j
#             if inp[j] not in x:
#                 x+=inp[j]
#             i+=1
#             j+=1
#         if x not in arr:
#             arr.append(x)
# print(arr)   
        
# inp="abc"
# n=[n*i for i in range(1,len(inp)+1)]
# print(n)







# for a in range(len(inp)):
#     m=0
#     n=0
#     x=inp[a]
#     for j in range(a,len(inp)+a):
#         if j>=len(inp):
#             m=0
#         else:
#             m=j
#         if inp[m] not in x:
#             x+=inp[m]

#         if len(x)==3:
#             arr.append(x)
#             x=""


            
        
    
       

# print(arr)



        
inp="abc"
arr=[]
for i in inp:
    count=0
    n=0
    while(count<len(inp)-1):
        str=i
        for j in range(len(inp)):
            if n>len(inp):
                n=0
            else:
                n=n
            if inp[n] not in str:
                str+=inp[n]
        arr.append(str)
        count+=1
        
print(arr)      




    
        

        
        

