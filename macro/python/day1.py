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


l1=[1,2,34]
# list modification
l1[0]=20
l1.append(204)
print(l1[2:4])
print(l1)


t1=(1,2,3,4)
t2=t1.__add__((20,30,50))
print(t1)
print(t2)
print(t2[2:6:2])


            


