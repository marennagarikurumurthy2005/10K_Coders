# string="madam"
# count=0
# l=len(string)
# new_string=""
# while count<l:
#     new_string=string[count]+new_string
#     count+=1
# print(new_string)


# # palindrome of not

# if string==new_string:
#     print("given string is a palindrome")
# else:
#     print("Not a palindrome ")

# number_of_vowels=0
# vowels=["a","e","i","o","u"]
# for i in string:
#     if i in vowels:
#         number_of_vowels+=1
# print(number_of_vowels)


# number_of_cons=0
# vowels=["a","e","i","o","u"]
# for i in string:
#     if i not in vowels:
#         number_of_cons+=1
# print(number_of_cons)


# vo=0
# co=0
# for i in string:
#     if i in vowels:
#         vo+=1
#     else:
#         co+=1
# print(vo,co)

# list_ele=["Hi","MK","How","R","U"]
# list_text=""
# for i in list_ele:
#     list_text=list_text+i+" "
# print(list_text)


# text="animalplant"
# dici={}
# for i in text:
#     if i in vowels:
#         if i in dici:
#             dici[i]=dici[i]+1
#         else:
#             dici[i]=1
# print(dici)

    
# remove vowels from a string

# string="kurumurthymarennagari"
# vowels=["a","e","i","o","u"]
# new_string=""
# for i in string:
#     if i not in vowels:
#         new_string=new_string+i
# print(new_string)


# changeing upper case to lower case
a=(ord("A"))
b=(ord('a'))
dif=b-a
print(dif)
string="kurumurthymarennagari"
new_string=""
for i in string:
    x=ord(i)
    new_string=new_string+chr(x-dif)
print(new_string)

string="KURUMURTHYMARENNAGARI"
new_string=""
for i in string:
    x=ord(i)
    new_string=new_string+chr(x+dif)
print(new_string)

string="KURUMURTHY MARENNAGARI"
new_string=""
for i in string:
    if i!=" ":
        new_string=new_string+i
print(new_string)




def web():

    site="https://srevathi.vercel.app/"
    mail1="marennagarikurumurthy2005@gmail.com"
    password1="murthy@0903"
    mail2="sirigadderevathi@gmail.com"
    password2="revathi@1909"

    
















