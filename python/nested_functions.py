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

def parent():
    a=40
    def child():
        nonlocal a
        a+=1
        print(a)
    child()
parent()


a=40
def parent():
    def child():
        global a
        a+=1
        print(a)
    child()
parent()



