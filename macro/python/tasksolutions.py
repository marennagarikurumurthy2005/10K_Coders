# Task 1: Student Data Management System
# Objective: Build a program to store and manage student academic data.
# Input:
# ● Student name
# ● Roll number
# ● List of subjects (may contain duplicates)
# ● Marks for each subject
# Expected Output:
# ● Student details printed clearly
# ● Duplicate subjects removed
# ● Subjects mapped with marks
# Mandatory Requirements:
# ● Use list, set, and dictionary
# ● Follow PEP 8 naming conventions


# data=[]
# while True:
#     dici = {}
#     print("enter 1 for insert 2 for display details:")
#     userinp=input()
#     if userinp=="1":
#         name=input("Enter Name:")
#         roll=input("Enter Roll Number:")
#         marks={}
#         sub=['maths','physics','chemistry']
#         for i in range(len(sub)):
#             marks_input=int(input(f"Enter marks obtained in {sub[i]}:"))
#             marks[sub[i]]=marks_input
#         dici["name"]=name
#         dici["roll"]=roll
#         dici['marks']=marks
#         print("details added successfully")

#         data.append(dici)

#     elif userinp=="2":
#         print(data)
    
#     else:
#         print("Wrong choice")
#         break;



# Task 2: Flexible Calculator
# Objective: Create a calculator that supports dynamic operations.
# Input:
# ● Operation type (add, multiply, factorial)
# ● Variable number of inputs
# Expected Output:
# ● Correct calculation result
# Mandatory Requirements:
# ● Use *args for arithmetic operations
# ● Use recursion for factorial
# ● Use lambda functions


# def factorial(num):
#     if num==1:
#         return num
#     return num*factorial(num-1)

# square=lambda x: x**2

# def getting(*data):
#     for i in data:
        
#         try:
#             ren=eval(i)
#             print(ren)
#         except:
#             print("invalid expression")
        


# while True:

#     choice=input("enter 1 for arithmetic(+,-,*,/) , 2 for others")

#     if choice=="1":
#         exp=input("Enter Expression for multi operations seperate with comas")
#         cal=tuple(exp.split(","))
#         print(exp)
#         print(cal)
#         getting(*cal)

#     elif choice=="2":
#         built_op=input("enter 1 for factorial, 2 for square root")
#         if built_op=="1":
#             fac=int(input("enter number for factorial calculation:"))

#             if fac>0:
#                 res=factorial(fac)
#                 print(res)

#             elif fac==0:
#                 print("1")
#             else:
#                 print("Not able to calculate")
                

#         elif built_op=="2":
#             sq=int(input("enter number"))
#             asqr=square(sq)
#             print(asqr)
#     else:
#         print("invalid choice")
#         break
        

# Task 3: Safe File Reader
# Objective: Read files safely with proper error handling.
# Input: File name
# Expected Output: File contents or user-friendly error message
# Mandatory Requirements:
# ● Use with statement
# ● Handle FileNotFoundError
# ● Use finally

# kohli=r'C:\Users\maren\10KCoders\macro\python\kohlis.txt'

# try:
#     with open(kohli,'r') as f:
#         data=f.readline()
#         print(data)
# except Exception as e:
#     print(f'Error {e}')

# finally:
#     print("Exicution completed")


# # Task 4: Text File Analyzer
# # Objective: Analyze a text file efficiently.
# # Input: Text file
# # Expected Output:
# # ● Line count
# # ● Word count
# # Mandatory Requirements:
# # ● Use generator for file reading
# # ● Use list comprehension
# # ● Use decorator to log execution time

# from time import perf_counter

# file=r"C:\Users\maren\10KCoders\macro\python\kohli.txt"

# def timer(func):
#     def wrapper(args):
#         start=perf_counter()
#         res=func(args)
#         end= perf_counter()
#         print(end-start)
#         return res
#     return wrapper
    
# def reading(file_name):
#     with open(file_name,'r') as file:
#         for line in file:
#             yield line

# @timer
# def func(file_name):
#     word_count=0
#     line_count=0
#     for line in reading(file_name):
#         line_count+=1
#         words=[word for word in line.split()]
#         word_count+=len(words)
#     print(line_count)
#     print(word_count)

# try:
#     func(file)
# except Exception as e:
#     print(e)
# finally:
#     print("exicution completed")








# from time import perf_counter
# kohli=r'C:\Users\maren\10KCoders\macro\python\kohli.txt' 
# try:
#     line_count=0
#     word_count=0
#     start=perf_counter()
#     def genrator(func):
#         with open(kohli,'r') as file:
#             data=file.readlines()
#             for line in data:
#                 line_count+=1
#                 yield line
#             func()
#     end=perf_counter()
#     @genrator
#     def timer(start,end):
#         return end-start
#     timer(start,end)
#     # time=0
#     # gen=genrator(time)
#     print(line_count)
#     print(word_count)
# except Exception as e:
#     print(e)
# finally:
#     print("End of exicution")




# from time import perf_counter
# kohli=r'C:\Users\maren\10KCoders\macro\python\kohli.txt' 
# try:
#     line_count=0
#     word_count=0
#     def genrator(time):
#         with open(kohli,'r') as file:
#             for line in file:
#                 print(line)
#                 line_count=1
#                 time()
#                 yield line
#     @genrator
#     def timer():
#         t=perf_counter()
#         print(t)
#     timer()
    
#     gen=genrator(timer)

#     for i in range(line_count):
#         data=next(gen)
#         for i in data:
#             word_count+=1
    
#     print(word_count)
#     print(line_count)
# except Exception as e:
#     print(f"Error",e)
# finally:
#     print("Completion of process")
    


# Task 5: Mutability & Scope Demo
# Objective: Demonstrate mutability and scope behavior.
# Input: List and tuple
# Expected Output:
# ● List modification reflected
# ● Tuple unchanged
# ● Slicing results


# l1=[1,2,34]
# # list modification
# l1[0]=20
# l1.append(204)
# print(l1[2:4])
# print(l1)


# t1=(1,2,3,4)
# t2=t1.__add__((20,30,50))
# print(t1)
# print(t2)
# print(t2[2:6:2])


# Task 6: Mini Banking System
# Objective: Build a basic banking system using OOP.
# Mandatory Requirements:
# ● Base class Account
# ● Child class SavingsAccount
# ● Private balance variable


# class Account:
#     def __init__(self):
#         self.bankname="SBI"
#         self.branch="Kothakota"
#     def bank_details(self):
#         print(self.bankname)
#         print(self.branch)

# class SavingsAccount(Account):
#     def __init__(self):
#         super().__init__()
#         self.username="Murthy"
#         self.acc_number="XXXXXXXX7125"
#         self.__savings=5000
    
#     def balance(self):
#         super().bank_details()
#         print(self.username)
#         print(self.acc_number)
#         print(self.__savings)

# obj=SavingsAccount()
# obj.balance()

        
        
# Task 7: Resource Manager & Iterator
# Objective: Implement custom context manager and iterator

# 1 custom iterator to print even numbers from 1 to n


# class even:
#     def __init__(self,num):
#         self.num=num
#         self.start=0

#     # used to create a iterator
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         while self.start<self.num:
#             value=self.start
#             self.start+=1
#             if value%2==0:
#                 return value
#         else:
#             raise StopIteration
        



        # self.value=self.start
        
        # if self.value>=self.num:
        #     raise StopIteration

        # if self.value %2==0:
        #     self.start+=1
        #     return self.value
        # else:
        #     self.start+=1
        #  it is returning none at even number

# iterator=even(10)
# for i in iterator:
#     print(i)


# file_path=r"C:\Users\maren\10KCoders\macro\python\kohli.txt"
# class myContext:
#     def __init__(self,file_name):
#         self.file_name=file_name
#     def __enter__(self):

#         self.data=open(self.file_name,'r')
#         print("file opened")
#         return self.data
    
#     def __exit__(self, exc_type, exc, tb):
#         self.data.close()
#         print("file closed")
#         if exc_type is not None:
#             print(exc_type)
    
# with myContext(file_path) as c:
#     raw=c.read()
#     print(raw)
    


# Task 8: Inventory Management System
# Objective: Manage inventory using stacks, queues, and dictionaries.  
#



# from collections import deque
# from abc import ABC,abstractmethod

# class Inventory(ABC):
    
#     @abstractmethod
#     def item_sale(self,item="santoor"):
#         pass
    
#     @abstractmethod
#     def add_item(self,item):
#         pass

# class Stack_implementation(Inventory):
#     def __init__(self):
#         self.soaps=["SANTOOR","ASSURE"]
#     def item_sale(self):
#         if len(self.soaps)>0:
#             x=self.soaps.pop()
#             return x,"take the soap"
#         else:
#             return "Soaps Out of Stock"
#     def add_item(self,item):
#         self.soaps.append(item)
#         return "Item added",self.soaps

# obj=Stack_implementation()
# x=obj.item_sale()
# print(x)

# class Queues_implementation(Inventory):
#     def __init__(self):
#         self.soaps=deque(["SANTOOR","ASSURE"])
#     def item_sale(self):
#         if len(self.soaps)>0:
#             x=self.soaps.popleft()
#             return x,"take the soap"
#         else:
#             return "Soaps Out of Stock"
#     def add_item(self,item):
#         self.soaps.append(item)
#         return "Item added",self.soaps
# obj=Queues_implementation()
# x=obj.add_item("LUX")
# print(x)



# class Dictonary_implementation(Inventory):
#     def __init__(self):
#         self.soaps={'SANTOOR':1, 'ASSURE':1, 'LUX':1}
    
#     def item_sale(self, item="santoor"):
#         if item in self.soaps:
#             if self.soaps[item]>0:
#                 self.soaps[item]-=1
#                 return "take the soap",item
            
#             else:
#                 return  item,"soaps outof stock"
#         else:
#             return item,"soaps out of stock"
    
#     def add_item(self, item):
#         if item in self.soaps:
#             self.soaps[item]+=1
#             return "soap added",self.soaps
#         else:
#             self.soaps[item]=1
#             return self.soaps

# obj=Dictonary_implementation()
# x=obj.add_item("LUX")
# print(x)  



import re

pattern1=r".*ERROR.*"
pattern2=r".*WARNING*."
file_path=r"C:\Users\maren\10KCoders\macro\python\app.log"

with open(file_path,'r') as file:
    data=file.readlines()
    # errors=list(filter(lambda line: re.match(pattern1,line),file))
    # warnings=list(filter(lambda line: re.match(pattern2,line),file))



errors=list(filter(lambda lines: re.match(pattern1,lines),data))
warnings=list(filter(lambda lines:re.match(pattern2,lines),data))
for i in errors:
    print(i,end="")     
print()
for j in warnings:
    print(j)       









        
        

        

        




        






        
    




            


