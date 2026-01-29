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

input=int(input("Enter Number:"))
temp=input
net=temp
l=0
while net>0:
    net//=10
    l+=1

sum=0
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



for i in str(input):
    sum+=int(i)**l

if sum==temp:
    print(f"{temp} is a Armstrong number")
else:
    print(f"{temp} is Not a armstrong number")
    





            
        
        





