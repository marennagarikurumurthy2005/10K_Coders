#  scope chaining is the access flow of the variables in the nester functions


# nested function 
# def parent():
#     print("Parent")
#     def child():
#         print("Child")
#     child()
# parent()


# scoping
#  function scoping , local scoping , global scoping 

# def parent():
#     print("trying to access ",a)
#     def child():
#         a=10
#         print(a)
#     child()
# parent()

#   the error 
#  File "c:\Users\maren\10KCoders\python\nested_functions.py", line 22, in <module>
#     parent()
#     ~~~~~~^^
#   File "c:\Users\maren\10KCoders\python\nested_functions.py", line 17, in parent
#     print("trying to access ",a)
#                               ^
# NameError: name 'a' is not defined

# def parent():
#     def child():
#         global a
#         #  now we cah use the a at any place but only to access not to edit
#         a=10
#         print(a)
#     child()
#     print("trying to access ",a)
# parent()

#  to update the value we use the nonlocal keyword

# def parent():
#     a=40
#     def child():
#         nonlocal a
#         a+=1
#         print(a)
#     child()
# parent()


# a=40
# def parent():
#     global a
#     a+=1
#     print(a)
#     def child():
#         print("yes")
#     child()
# parent()



# global is used to access and modify only which are in the global scope 
#  the nonlocal is used to access and modify the local scope variables

# for example

# global
# x=10
# def parent():
#     def child():
#         global x
#         x+=1
#         print(x)
#     def child2():
#         global x
#         x-=1
#         print(x)
#     return child,child2
# parent()[0]()
# parent()[1]()

# #  nonlocal

# def parent():
#     x=10
#     def child1():
#         nonlocal x
#         x+=1
#         print(x)
#     def child2():
#         nonlocal x
#         x-=1
#         print(x)
#     return child1,child2
# parent()[0]()
# parent()[1]()

x=0
def parent():
    def child():
        x=10
        print(x)
    return child()
parent()



# funtion method miss
def add():
    return 25+5
res=add()
print(res)








