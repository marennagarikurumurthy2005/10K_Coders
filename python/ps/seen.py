# # valid parenthesis

# exp="{([])}"

# is_valid=True
# stack=[]

# for i in exp:
#     if i in '([{':
#         stack.append(i)
#     else:
#         if len(stack)!=0:
#             if (i==')' and stack[-1]=='(') or (i=='}' and stack[-1]=='{') or (i==']' and stack[-1]=='['):
#                 stack.pop()
#             else:
#                 is_valid=False
#                 break
#         else:
#             is_valid=False
#             break
# if len(stack)!=0:
#     is_valid=False

# print(is_valid)


# sorting colors

# colors=[1,0,2,1,0,2]
# low=mid=0
# high=len(colors)-1

# while mid<=high:
#     if colors[mid]==0:
#         colors[mid],colors[low]=colors[low],colors[mid]
#         low+=1
#         mid+=1
#     elif colors[mid]==1:
#         mid+=1
#     else:
#         colors[high],colors[mid]=colors[mid],colors[high]
#         high-=1
# print(colors)


# s="fourtwosevensix"
# dici={
#     "one":'1',
#     "two":'2',
#     "three":'3',
#     "four":'4',
#     "five":'5',
#     "six":'6',
#     "seven":'7',
#     "eight":'8',
#     "nine":'9'
# }
# sub=""
# num=""
# for i in s:
#     sub+=i
#     if sub in dici:
#         num=num+dici[sub]
#         sub=""
# print(num)

# i=0
# j=1
# num=0
# while j<=len(s):
#     if s[i:j] in dici:
#         num=num*10+int(dici[s[i:j]])
#         i=j
#     else:
#         j+=1
# print(num)


# dici={}

# string="kurumurthy"
# vowels="aeiou"
# for i in string:
#     if i in vowels:
#         if i in dici:
#             dici[i]+=1
#         else:
#             dici[i]=1
# toatl_vowels=0
# for i in dici:
#     toatl_vowels+=dici[i]
# print(dici)
# print(toatl_vowels)


# dici={}
# string="kurumurthy"
# vowels="aeiou"
# for i in string:
#     if i not in vowels:
#         if i in dici:
#             dici[i]+=1
#         else:
#             dici[i]=1
# toatl_vowels=0
# for i in dici:
#     toatl_vowels+=dici[i]
# print(dici)
# print(toatl_vowels)

# s1="silent"
# s2="listen"
# dici1={}
# dici2={}

# for i in s1:
#     if i in dici1:
#         dici1[i]+=1
#     else:
#         dici1[i]=1
# for j in s2:
#     if j in dici2:
#         dici2[j]+=1
#     else:
#         dici2[j]=1
# if dici1==dici2:
#     print("anagram")
# else:
#     print("Not a anagram")

# l1=[1,3,6,8]
# l2=[1,6,2,9]
# dici={}
# newlist=[]
# for i in l1:
#     if i in dici:
#         dici[i]+=1
#     else:
#         dici[i]=1
# for i in dici:
#     if i in l2:
#         newlist.append(i)
# print(newlist)

# l1=[1,0,6,8,0,6]
# li1=[]
# li2=[]
# for i in l1:
#     if i==0:
#         li2.append(i)
#     else:
#         li1.append(i)
# print(li1+li2)

name="VaIsHnAvI"
# s1=""
# s2=""
# for i in name:
#     if i in "aeiou":
#         s2+=i
#     else:
#         s1+=i
# print(s1+s2)


dici={"u":0,"l":0}

for i in name:
    if 'A'<=i<='Z':
        dici["u"]+=1
    elif 'a'<=i<='z':
        dici['l']+=1
print(dici)
 

    


    

