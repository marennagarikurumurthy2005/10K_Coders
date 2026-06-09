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


data=[]
while True:
    dici = {}
    print("enter 1 for insert 2 for display details:")
    userinp=input()
    if userinp=="1":
        name=input("Enter Name:")
        roll=input("Enter Roll Number:")
        marks={}
        sub=['maths','physics','chemistry']
        for i in range(len(sub)):
            marks_input=int(input(f"Enter marks obtained in {sub[i]}:"))
            marks[sub[i]]=marks_input
        dici["name"]=name
        dici["roll"]=roll
        dici['marks']=marks
        print("details added successfully")

        data.append(dici)

    elif userinp=="2":
        print(data)
    
    else:
        print("Wrong choice")
        break;



            


