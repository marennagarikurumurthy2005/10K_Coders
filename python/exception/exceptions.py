


# input=int(input("Enter a number:"))
# try:
#     res=input/0
#     print(res)
# except:
#     print("zero division error")
# finally:
#     print("Execution completed")



# set=int(input("Enter a number:"))
# div=input("Enter a div:")
# try:
   
#     res=set/int(div)
#     print(res)
# except ZeroDivisionError:
#     print("Zero division error")
# except ValueError:
#     print("String is passes in div")

# finally:
#     print("Excution completed")


# l1=[1,5,6]
# num=3
# try:
#     print(l1[num])
# except IndexError:
#     print(f"the list has len of {len(l1)-1} but passed {num} as index value ")


# dici={"name":"Murthy","num":24}
# try:
#     print(dici["contact"])
# except KeyError:
#     print("Key not found")

# n={"name":"vishnu"}
# try:
#     print(n["age"])
# except KeyError:
#     print("key not found")


class Selection(Exception):
    pass

min_age=18
min_height=156
min_weight=65
# try:
#     age=int(input("age:"))
#     height=int(input("Height:"))
#     weight=int(input("weight:"))
#     if age>min_age and height>min_height and weight>min_weight:
#         print("selected")
#     else:
#         raise Selection("not eligible")
# except Selection as msg:
#     print(msg)


# try:
#     age=int(input("age:"))
#     height=int(input("Height:"))
#     weight=int(input("weight:"))
#     if age>min_age and height>min_height and weight>min_weight:
#         print("selected")
#     elif age<min_age and height>min_height and weight>min_weight:
#         raise Selection("Low age")
#     elif age>min_age and height<min_height and weight>min_weight:
#         raise Selection("Low height")
#     elif age>min_age and height>min_height and weight<min_weight:
#         raise Selection("low weight")
#     elif age<min_age and height<min_height and weight>min_weight:
#         raise Selection("Low age,height")
#     elif age<min_age and height>min_height and weight<min_weight:
#         raise Selection("Low age,weight")
#     elif age>min_age and height<min_height and weight<min_weight:
#         raise Selection("Low weight,height")
#     else:
#         raise Selection("low age,height,weight")
# except Selection as msg:
#     print(msg)
    
l=list(map(input().split()))

try:
    year=int(input("ENter year:"))
    skills=int(input("if yes 1, else 0:"))
    if year<=2026 and skills==1:
        print("you csn apply for this job")
    else:
        raise Selection("not eligible")
except Selection as m:
    print(m)










