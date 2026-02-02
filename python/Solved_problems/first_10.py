# #1
# def FlattenANestedList(nested_list):
#     """
#     nested_list: List[List[int]]
#     Returns: List
#     """
#     # 3: Implement your solution here
#     new_list=[]
#     for i in nested_list:
#         new_list+=[*i]

#     return new_list

# #2
# def maximumWealth(accounts):
#     """
#     accounts: List[List[int]]
#     Returns: int
#     """
#     # 3TODO: Implement your solution here
#     max_wealth=0
#     n=len(accounts)
#     for i in range(n):
#         m=len(accounts[i])
#         indisum=0
#         for j in range(m):
#             indisum+=accounts[i][j]
#         max_wealth=max(max_wealth,indisum)
#     return max_wealth

# #3

# def AntiDiagonalElements(mat):
#     """
#     mat: List[List[int]]
#     Returns: List[int]
#     """
#     # 3TODO: Implement your solution here
#     new_list=[]
#     n=len(mat)
    
#     if n>1:
#         for i in range(n):
#             for j in range(n):
#                 if  i+j==n-1:
#                     new_list.append(mat[i][j])
#     else:
#         new_list.append(mat[0][0])
#     return new_list


# #4

# def find_freq(nums, x):
#     """
#     nums: List[int]
#     x: int
#     Returns: int
#     """
#     # 3TODO: Implement your solution here
#     count=0
#     for i in nums:
#         if i==x:
#             count+=1
#     return count

# #5
# def amount_breaking(amount):
#     """
#     amount: int
#     Returns: List[List[int]]
#     """
#     # 3TODO: Implement your solution here
#     dici=[["1000's", 0], ["500's", 0], ["remaining", 420]]
#     while amount>=0:
#         if amount>=1000:
#             reminder=amount%1000
#             need=(amount-reminder)/1000
#             amount=reminder
#             dici[0][1]=int(need)
#         elif amount>=500 and amount<1000:
#             reminder=amount%500
#             need=(amount-reminder)/500
#             amount=reminder
#             dici[1][1]=int(need)
#         else:
#             dici[2][1]=amount
#             amount=-1
#     return dici

# #6 
# def MaxMinDifference(nums):
#     """
#     nums: List[int]
#     Returns: int
#     """
#     # 3TODO: Implement your solution here
#     mini=min(nums)
#     maxi=max(nums)
#     return maxi-mini


# #7
# def SumOfTwoLargestDigitsAmongThree(a, b, c):
#     """
#     a: int
#     b: int
#     c: int
#     Returns: int
#     """
#     # 3TODO: Implement your solution here
#     first_max=max(a,b,c)
#     mini=min(a,b,c)
#     second_max=((a+b+c)-(first_max+mini))
#     return first_max+second_max
#     pass


# #8

# def BubbleSort(nums):
#     """
#     nums: List[int]
#     Returns: int
#     """
#     # 3TODO: Implement your solution here
#     n=len(nums)
#     count=0
#     for i in range(n):
#         min=nums[i]
#         for j in range(0,n-i-1):
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
#                 count+=1
#     return count

# #9 


# def firstNonRepeatingChar(s):
#     """
#     s: str
#     Returns: int
#     """
#     # 3TODO: Implement your solution here
#     new_dici={}
#     n=len(s)
#     place=-1
#     new_var=""
#     for i in s:
#         if i in new_dici:
#             new_dici[i]+=1
#         else:
#             new_dici[i]=1
#     for i in new_dici:
#         if new_dici[i]<=1:
#             new_var=i
#             break
#     for i in range(n):
#         if new_var==s[i]:
#             place=i
#             break
#     return place

# name="Madhu"
# print()
# dici={"name":"MK","Number":724,"add":"Nirven"}
# print(dici)
# new_dici={}
#     place=-1
#     for i in s:
#         if i in new_dici:
#             new_dici[i]+=1
#         else:
#             new_dici[i]=1
#     for i in new_dici:
#         if new_dici[i]<=1:
#             place=index(s[new_dici[i]])
#     return place



#10


def sumOfDigits(n):
    """
    n: int
    Returns: int
    """
    # TODO: Implement your solution here
    if n==0:
        return n
    reminder=n%10
    n=n//10
    return reminder+sumOfDigits(n)

# def fun(n):
#     if n<10:
#         return n
#     reminder=n//10

# print(512%10)

