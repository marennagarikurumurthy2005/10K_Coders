# string="MK's"
# new_string=""
# print(ord("A"))
# print(ord("Z"))
# print(ord("a"))
# print(ord("z"))
# print(ord("0"))

# for i in string:
#     a=ord(i)
#     if a>=65 and a<=122:
#         new_string=new_string+i
# print(new_string)



# # remove punctuations from a sentence
# name=""""Hi goodmorning i'm Kurumurthy marennagari. i'm from wnaparty-dist ! kkt_mandal,Nirven@#$%^"""
# new_name=""
# for i in name:
#     if i not in """",.:;'"!@#$%^&*()-_""":
#         new_name=new_name+i
# print(new_name)

string="1234"
print(ord("A"))
print(ord("Z"))
print(ord("a"))
print(ord("z"))
print(ord("0")) 
print(ord("9")) 


digits=True
for i in string:
    a=ord(i)
    if a<48 or a>57:
        digits=False
        break
if digits:
    print("True")
else:
    print("False")


        
st=True
for i in string:
    a=ord(i)
    if a<65 or a>122:
       st=False
       break
if st:
    print("True")
else:
    print("False")


string="MK"






