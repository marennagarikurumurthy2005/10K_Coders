# # #1 
# # def countVowels(s):
# #     """
# #     s: str
# #     Returns: int
# #     """
# #     # 1TODO: Implement your solution here
# #     vowels=["a","A","e","E","i","I","o","O","u","U"]
# #     count=0
# #     n=len(s)
# #     for i in range(n):
# #         if s[i]!=" " and s[i] in vowels:
# #             count+=1

# #     return count


# input= "I enjoy coding"
# words=input.split()

# dici={}
# for i in words:
#     if i in dici:
#         pass
#     else:
#         dici[i]=len(i)
# text=["0"]
# maxi=0
# for i in dici:
#     if dici[i]>maxi:
#         maxi=dici[i]
#         text[0]=i
# print(text[0])





# # def longestWord(sentence):
# #     """
# #     sentence: str
# #     Returns: str
# #     """
# #     # 1TODO: Implement your solution here
# #     longest=""
# #     words=sentence.split()
# #     for word in words:
# #         if len(word)>len(longest):
# #             longest=word
# #     return longest



# Rats and Food Distribution
# EASY
# Problem Description
# Given r rats and unit amount of food consumed by each rat, and an array arr representing the food available at each house, determine the minimum number of consecutive houses starting from the first house that have sufficient food for all rats.

# If the array is null, return -1.
# If the total food from all houses is insufficient, return -1.
# Function Signature
# RatsFoodDistribution(r: int, unit: int, arr: array<int>) → int
# Input
# r → number of rats (positive integer)
# unit → amount of food each rat consumes (positive integer)
# arr → array of positive integers representing the amount of food in each house
# Output
# Minimum number of consecutive houses (starting from the first house) needed to feed all rats, or -1 / 0 as described in the problem statement.
# Examples
# Example 1
# Input: r = 7 unit = 2 arr = [2, 8, 3, 5, 7, 4, 1, 2]

# Output: 4

# Explanation: Total food required = 7 * 2 = 14 Sum of food in first 4 houses = 2 + 8 + 3 + 5 = 18 ≥ 14 Hence, minimum number of houses = 4

# Example 2
# Input: r = 5 unit = 3 arr = [1, 2, 3, 1, 2, 4]

# Output: 5

# Explanation: Total food required = 5 * 3 = 15 Sum of food in first 5 houses = 1 + 2 + 3 + 1 + 2 = 9 < 15 Sum of first 6 houses = 1 + 2 + 3 + 1 + 2 + 4 = 13 < 15 All houses combined = 13 < 15, so return 0

# Example 3
# Input: r = 3 unit = 1 arr = [2, 2, 2]

# Output: 1

# Explanation: Total food required = 3 * 1 = 3 Sum of food in the first house = 2 < 3 Sum of first 2 houses = 2 + 2 = 4 ≥ 3 Hence, minimum number of houses = 2

r = 7 
unit = 2 
arr = [2, 8, 3, 5, 7, 4, 1, 2]
fr=r*unit
sum=0
ind=-1
for i in range(len(arr)):
    sum+=arr[i]
    if fr>sum:
        ind=i+1
print(ind)
