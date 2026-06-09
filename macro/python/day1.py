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


def factorial(num):
    if num==1:
        return num
    return num*factorial(num-1)

square=lambda x: x**2

def getting(*data):
    for i in data:
        
        try:
            ren=eval(i)
            print(ren)
        except:
            print("invalid expression")
        


while True:

    choice=input("enter 1 for arithmetic(+,-,*,/) , 2 for others")

    if choice=="1":
        exp=input("Enter Expression for multi operations seperate with comas")
        cal=tuple(exp.split(","))
        print(exp)
        print(cal)
        getting(*cal)

    elif choice=="2":
        built_op=input("enter 1 for factorial, 2 for square root")
        if built_op=="1":
            fac=int(input("enter number for factorial calculation:"))

            if fac>0:
                res=factorial(fac)
                print(res)

            elif fac==0:
                print("1")
            else:
                print("Not able to calculate")
                

        elif built_op=="2":
            sq=int(input("enter number"))
            asqr=square(sq)
            print(asqr)
    else:
        print("invalid choice")
        break
        

        


            


