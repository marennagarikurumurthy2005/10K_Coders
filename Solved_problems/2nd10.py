# #1 
# def countVowels(s):
#     """
#     s: str
#     Returns: int
#     """
#     # 1TODO: Implement your solution here
#     vowels=["a","A","e","E","i","I","o","O","u","U"]
#     count=0
#     n=len(s)
#     for i in range(n):
#         if s[i]!=" " and s[i] in vowels:
#             count+=1

#     return count


input= "I enjoy coding"
words=input.split()

dici={}
for i in words:
    if i in dici:
        pass
    else:
        dici[i]=len(i)
text=["0"]
maxi=0
for i in dici:
    if dici[i]>maxi:
        maxi=dici[i]
        text[0]=i
print(text[0])





# def longestWord(sentence):
#     """
#     sentence: str
#     Returns: str
#     """
#     # 1TODO: Implement your solution here
#     longest=""
#     words=sentence.split()
#     for word in words:
#         if len(word)>len(longest):
#             longest=word
#     return longest