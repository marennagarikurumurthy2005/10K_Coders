input=input("Enter Password:")
special_char=0
charu=0
charl=0
num=0

# print(ord("A"))
# print(ord("Z"))
# print(ord("a"))
# print(ord("z"))
# print(ord("0"))
# print(ord("9"))

for i in input:
    if ord(i)>=65 and ord(i)<=90:
        charu+=1
    elif ord(i)>=97 and ord(i)<=122:
        charl+=1
    elif ord(i)>=48 and ord(i)<=57:
        num+=1
    else:
        special_char+=1

if special_char>=1 and charu>1 and charl>1 and num>1:
    print("Strong Password")
else:
    print("Not Strong")


    