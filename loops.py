###---------------------------------------------DAY 1

# for i in range(1000):
#     print(i+1)


# i=145
# print(i)
# count=0
# while i>0:
#     count+=1
#     i//=10
# print(count)

# for i in range(100,0,-1):
#     print(i)

# i=100
# while i>0:
#     print(i)
#     i-=1


# i=int(input())
# count=0
# if i<10:
#     count+=1
# else:
#     while i>0:
#         count+=1
#         i//=10
# print(count)



# sum=0
# for i in range(101):
#     sum+=i

# print(sum)

# i=1 
# while i<=100:
#     sum+=i
#     i+=1
# print(sum)

# sum=0
# for i in range(40,61):
#     sum+=i

# print(sum)
# sum=0
# i=40
# while i<=60:
#     sum+=i
#     i+=1
# print(sum)


# sum=(100*101)/2
# print(int(sum))

# even numbers
# for i in range(0,201,2):
#     print(i)
# odd

# for i in range(1,201,2):
#     print(i)

# using while loop
# i=1
# while i<=100:
#     if i%2==0:
#         print(i)
#     i+=1

# i=1
# while i<=100:
#     if i%2!=0:
#         print(i)
#     i+=1



###---------------------------------------------DAY 2

# maxi=1000
# total=0
# for i in range(maxi+1):
#     if i %2==0:
#         total+=i
# print(total)


# maxi=1000
# total=0
# for i in range(maxi+1):
#     if i %2!=0:
#         total+=i
# print(total)

# for i in range(1,11):
#     print(f"multiplication table of {i}")
#     for j in range(1,11):
#         print(f"{i}X{j}={i*j}")

# user=int(input())
# count=0
# for i in range(1,user+1):
#     count+=1

# print(count)

# fact=1
# if user==0:
#     fact=1
# else:
#     for i in range(1,user+1):
#         fact*=i
# print(fact)


# num=int(input())
# count=0
# while num>0:
#     count+=1
#     num//=10
# print(count)


# num=int(input())
# count=0
# sum=0
# while num>0:
#     rem=num%10
#     sum+=rem
#     num//=10
# print(sum)



# DAY 2 part 2------------------------------------------------



# new_num=0
# num=123
# while num>0:
#     rem=num%10
#     num//=10
#     new_num=new_num*10+rem
# print(new_num)


# user=int(input())
# maxi=0
# extra=0
# while user>0:
#     extra=user%10
#     if maxi>=extra:
#         maxi=maxi
#     else:
#         maxi=extra
#     user//=10
# print(maxi)


# user=int(input())
# mini=9
# extra=0
# while user>0:
#     extra=user%10
#     if mini<=extra:
#         mini=mini
#     else:
#         mini=extra
#     user//=10
# print(mini)




# new_num=0
# num=12321
# temp=num
# while num>0:
#     rem=num%10
#     num//=10
#     new_num=new_num*10+rem
# print(new_num)
# if new_num==temp:
#     print("palin")
# else:
#     print("not a palin")


# Day3 Phase-1----------------------------------------------

# num=int(input())
# count=0
# if num<=1:
#     count=0
# else:
#     for i in range(2,num//2):
#         if num%i==0:
#             count+=1
#             break
# if count<=0:
#     print("prime")
# else:
#     print("Not a prime")


# for i in range(1,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)


# num=5
# net=2
# count=0
# while net<num:
#     if num%net==0:
#         count+=1
#         break
#     net+=1
# if count<=0:
#     print("Prime")
# else:
#     print("Not a prime")


# num=10
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# print(count)



# for i in range(1,num+1):
#     if num%i==0:
#         print(i)
        
# Day3 phase-2---------------------------------------------------------------
# num=27
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum+=i
# if sum==num:
#     print("Perfect Number")
# else:
#     print("Not a perfect Number")

# for i in range(1,10001):
#     sum=0
#     for j in range(1,i):
#         if i%j==0:
#             sum+=j
#     if i==sum:
#         print(i)


# strong numbers validation
# factorial of a number with individual digits as 
# 145 as 1!+4!+5! must equals with 145
# num=145
# temp=num
# sum=0
# while num>0:
#     rem=num%10
#     num//=10
#     net=1
#     for i in range(1,rem+1):
#         net*=i
#     sum+=net
# if sum==temp:
#     print("Strong Number")
# else:
#     print("Not a strong number")



# for i in range(1,1000000):
#     temp=i
#     sum=0
#     while i>0:
#         rem=i%10
#         i//=10
#         net=1
#         for j in range(1,rem+1):
#             net*=j
#         sum+=net
#     if sum==temp:
#         print(temp)

    

#  Day 4 Phase 1--------------------------------------------------------------

# input=int(input("Enter Number:"))
# temp=input
# net=temp
# l=0
# while net>0:
#     net//=10
#     l+=1

# sum=0
# while input>0:
#     rem=input%10

#     sum+=rem**l

#     input//=10
# if sum==temp:
#     print(f"{temp} is a Armstrong number")
# else:
#     print(f"{temp} is Not a armstrong number")

# for i in range(l):
#     get=input%10
#     sum+=get**l
#     input//=10

# if sum==temp:
#     print(f"{temp} is a Armstrong number")
# else:
#     print(f"{temp} is Not a armstrong number")



# for i in str(input):
#     sum+=int(i)**l

# if sum==temp:
#     print(f"{temp} is a Armstrong number")
# else:
#     print(f"{temp} is Not a armstrong number")



#  DAY 4 phase 1----------------------------------------------

# print(ord("a"))
#  print the capital alphabets from A-Z
# for i in range(26):
#     print(chr(i+65))

# for i in range(26):
#     print(chr(i+97))


# Count even digits in a number

# num=152478
# count=0
# while num>0:
#     rem=num%10
#     num//=10
#     if rem%2==0:
#         count+=1
# print(count)


# num=123579
# count=0
# while num>0:
#     rem=num%10
#     num//=10
#     if rem%2!=0:
#         count+=1
# print(count)


# num=156
# count=0
# while num>0:
#     rem=num%10
#     num//=10
#     if rem%5==0: # if rem==5:
#         count+=1
# print(count)


# finding the second largest digit in a number
# brute force
# num=int(input("Enter Number:"))
# largest=0
# second_largest=0
# while num>0:
#     rem=num%10
#     num//=10
#     if rem>largest:
#         second_largest=largest
#         largest=rem
        
#     if second_largest>largest and rem>second_largest:
#         second_largest=rem
        
    
# print(second_largest)
    





# method 1 using inbuilt functions
# num=int(input("Enter Number:"))
# list=[]
# while num>0:
#     rem=num%10
#     num//=10
#     list.append(rem)
#     list.sort()
# print(list[-2])

# composite number
# num=2
# count=0
# for i in range(2,num):
#     if num%i==0:
#         count+=1
#         break
# if count==1:
#     print("Composite")
# else:
#     print("Not a composite")

# composite numbers from 1 to 100
# for i in range(1,100):
#     count=0
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#             break
#     if count==1:
#         print(i)


       
#Day % phase 1=============================================================
# print(ord("a"))


# for i in range(26):
#     if (i+65)%2==0:
#         print(chr(i+65))

# print("ODD Alphabets")
    
# for j in range(26):
#     if (j+65)%2!=0:
#         print(chr(j+65))

# for i in range(26):
#     if (i+97)%2==0:
#         print(chr(i+97))
# for j in range(26):
#     if (j+97)%2!=0:
#         print(chr(j+97))



#  Root number ---------------------------------------------------------------

# while num>9:
#     sum=0
#     while num>0:
#         rem=num%10
#         num//=10
#         sum+=rem
#     num=sum

# print(num)

# Magical number---------------------------------------------------------------

# def net(data):
#     if data==0:
#         return data
#     else:
#         rem=data%10
#         data//=10
#         return rem+net(data)
    

# num=int(input("Enter a number:"))
# while num>9:
#     num=net(num)
# print(num)

# if num==1:
#     print("magical number")
# else:
#     print("Not a magical number")

# sum=0
# for i in range(10):
#     sum+=i
# print(sum)


#Day5 phase1=================================================
#fib sequence below the num n

# n=5
# c=0
# a,b=0,1
# c=a+b
# print(a,b)
# while c<n:
#     print(c)
#     a=b
#     b=c
#     c=a+b


# fib upto length n
# n=15
# a,b=0,1
# for i in range(n):
#     print(a)
#     a,b=b,a+b


# fib num less than n
# n=15
# a,b=0,1
# for i in range(n):
#     if b<n:
#         print(a,end=" ")
#         a,b=b,a+b
#     else:
#         break

#fib upto len n

# n=15
# a,b=0,1
# print(a)
# print(b)
# count=2

# for i in range(2,n):
#     c=a+b
#     print(c)
#     a=b
#     b=c
#     count+=1
# print(c)

# print(count)

    
# n = int(input())
# temp = n
# sum = 0
# while n>0:
#     rem = n%10
#     n//=10
#     sum+=rem
# if temp%sum==0:
#     print("Harshad number")
# else:
#     print("not a harshad number")




# num1=10
# num2=20
# # divi=max(num1,num2)
# sum=1

# for i in range(2,max(num1,num2)):
#     if num1%i==0 or num2%i==0:
#         # print(i)
#         # break
#         sum*=i
#         # divi=min(divi,i)

# print(sum)       
# # print(divi)


#  Day 6 phase 1=========================================================================
# for i in range(1,100):
#     square=i**2
#     sum=0
#     while square>0:
#         rem=square%10
#         sum+=rem
#         square//=10
#     if i==sum:
#         print(i)


#  LCM of a number

# num1=2
# num2=3
# largest=max(num1,num2)
# pro=num1*num2
# while largest<=pro:
#     if largest%num1==0 and largest%num2==0:
#         print(largest)
#         break
#     largest+=1

# way2

# largest=max(num1,num2)

# while True:
#     if largest%num1==0 and largest%num2==0:
#         print(largest)
#         break
#     largest+=1

# # way3 

# for i in range(max(num1,num2),pro+1):
#     if i%num1==0 and i%num2==0:
#         print(i)
#         break


# HCF
# num1=18
# num2=27
# hcf=0
# num3=min(num2,num1)
# for i in range(num3,0,-1):
#     if num1%i==0 and num2%i==0:
#         print(i)
#         break


# num=15
# dub=0
# while num>0:
#     rem=num%10
#     dub=dub+rem
#     num//=10
# print(dub)
# print(oct(num))


#Octal number

num=153
occt=""
while num>0:
    rem=num%8
    occt=str(rem)+occt
    num//=8
print(occt)













    
    
        
        
















            
        
        





