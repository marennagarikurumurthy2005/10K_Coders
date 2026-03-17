# # # remove the spaces with hyphens?
# # Input:  "Murthy is learning python 123"
# # Output: "Murthy-is-learning-python-123"

# text="Murthy is learning python 123"
# new_text=""
# for i in text:
#     if i==" ":
#         new_text=new_text+"-"
#     else:
#         new_text=new_text+i
# print(new_text)

# # # split the words at spaces?
# # Input:  "Murthy is learning python 123"
# # Output: ['Murthy', 'is', 'learning', 'python', '123']


# new_words=[]
# word=""
# for i in text:
    
#     if i==" ":
#         new_words.append(word)
#         word=""
#     else:
#         word=word+i
# print(new_words)


# # # find the length of string with len method?
# # Input:  "Murthy123"
# # Output: 9

# data="Murthy123"
# print(len(data))

# count=0
# for i in data:
#     count+=1
# print(count)



# # # count the frequency of characters in a string?
# # Input:  "Murthy123Murthy"
# # Output:
# # M : 2
# # u : 2
# # r : 2
# # t : 2
# # h : 2
# # y : 2
# # 1 : 1
# # 2 : 1
# # 3 : 1

# nett="Murthy123Murthy"
# dici={}
# for i in nett:
#     if i in dici:
#         dici[i]+=1
#     else:
#         dici[i]=1
# for i in dici:
#     print(f"{i} : {dici[i]}")



# # # remove all vowels from a string?
# # Input:  "Murthy is coding in python"
# # Output: "Mrthy s cdng n pythn"
# remvow="Murthy is coding in python"
# sol=""
# for i in remvow:
#     if i not in "a,e,i,o,u":
#         sol=sol+i
# print(sol)

# # # remove the digits from a string?
# # Input:  "Murthy123python456"
# # Output: "Murthypython"

# ddel="Murthy123python456"
# sol=""
# for i in ddel:
#     if i not in "0123456789":
#         sol=sol+i
# print(sol)


# # # find the last occured vowel in a string?
# # Input:  "Murthy learning python"
# # Output: "o"

# input= "Murthy learning python"
# for i in range(len(input)-1,-1,-1):
#     if input[i] in "a,e,i,o,u":
#         print(input[i])
#         break


# # # find the first occured vowel in a string?
# # Input:  "Murthy learning python"
# # Output: "u"

# input= "Murthy learning python"
# for i in range(len(input)):
#     if input[i] in "a,e,i,o,u":
#         print(input[i])
#         break


# anagrams]
# st1="listen"
# st2="silent"
# dici1={}
# dici2={}
# for i in st1:
#     if i in dici1:
#         dici1[i]+=1
#     else:
#         dici1[i]=1
# for i in st2:
#     if i in dici2:
#         dici2[i]+=1
#     else:
#         dici2[i]=1
# if dici1==dici2:
#     print("anagrams")
# else:
#     print("not a anagram")

string="krumrthy"
flag=0
for i in range(len(string)):
    for j in range(i+1,len(string)):
        if string[i]==string[j]:
            print(string[i])
            flag=1
            break
    if flag:
        break

# res=""
# flag=0
# for i in range(len(string)):
#     list=[]
#     for j in range(i,len(string)):
#         list.append(string[j])
#     if string[i] not in list:
#         print(string[i])
#         break


string="kurumrkthy"
freq={}
for i in string:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in freq:
    if freq[i]==1:
        print(i)
        break     
