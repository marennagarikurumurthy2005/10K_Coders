# functions are created using def key word 
# user defined , predefined

# pi=3.14
# square=2
# def area_of_circle():
#     print(pi*5**square)

# def area_of_trep():
#     par=10
#     hei=10
#     print(0.5*2*par*hei)

# def area_of_rect():
#     print(5*10)

# def area_of_triangle():
#     print(0.5*5*4)

# def area_of_square():
#     print(5**square)

# def perimeter_of_rectange():
#     print(2*(2+6))

# def perimeter_of_square():
#     print(4*2)

# def peri_of_tri():
#     print(5+6+4)

# def perimeter_of_circle():
#     print(2*pi*5)

# def peri_trepi():
#     print()


# area_of_circle()
# area_of_rect()
# area_of_square()
# area_of_triangle()
# area_of_trep()
# peri_of_tri()
# perimeter_of_rectange()
# perimeter_of_square()
# perimeter_of_circle()

# DAY3 ses1============================================

# sum of n natural numbers
# def sum(num):
#     sum=0
#     for i in range(num+1):
#         sum+=i
#     return sum
# res=sum(int(input("Enter N:")))
# print(res)


#all even number from 1 to n

# def even(num):
#     for i in range(1,num+1):
#         if i%2==0:
#             print(f"{i} is even")

# even(100)

# def odd(num):
#     for i in range(1,num+1):
#         if i%2!=0:
#             print(i)
# odd(100)
 

# sum of odd numbers
# def oddsum(num):
#     sum=0
#     for i in range(1,num+1):
#         if i%2!=0:
#             sum+=i
#     print(sum)

# oddsum(100)


# def evensum(num):
#     sum=0
#     for i in range(1,num+1):
#         if i%2==0:
#             sum+=i
#     print(sum)

# evensum(100)

# def table(num):
#     for i in range(1,num+1):
#         print(f"{i} Multiplication Table-------------------")
#         print("")
#         for j in range(1,11):
#             print(f"{i} X {j} = {i*j}")
        


# table(10)


# def countNum(n):
#     count=0
#     for i in range(n):
#         count+=1
#     print(count)
# countNum(100)


# factorial of a number

# def fact(num):
#     if num==1:
#         return num
#     else:
#         return num*fact(num-1)
# res=fact(5)
# print(res)


# def countDig(num):
#     count=0
#     while num>0:
#         count+=1
#         num//=10
#     return count
# res=countDig(156)
# print(res)


# def countDig(num):
#     sum=0
#     while num>0:
#         rem=num%10
        
#         sum+=rem
#         num//=10
#     return sum
# res=countDig(156)
# print(res)


# check prime number

# def checkPrime(num):
#     flag=0
#     for i in range(2,num):
#         if num%i==0:
#             flag=1
#             break
#     if flag==0:
#         print("prime")
#     else:
#         print("Not a prime")


# checkPrime(int(input("Enter number to check:")))

# find the the number is a armstrong number or not 

# def checkArms(num):
#     l=len(str(num))
#     temp=num
#     sum=0
#     while num>0:
#         rem=num%10
#         sum+=rem**l
#         num//=10
#     if sum==temp:
#         print("ARMS")
#     else:
#         print("NOT ARMS")

# checkArms(int(input("ENTER NUMBER :")))


# check the number forms palindrome or not 
# def checkPalin(num):
#     sum=0
#     temp=num
#     while num>0:
#         rem=num%10
#         sum=sum*10+rem
#         num//=10
#     return sum
# num=int(input("Enter number:"))
# res=checkPalin(num)
# print(True if res==num else False)

# def fact_Count(num):
#     count=1
#     for i in range(2,num+1):
#         if num%i==0:
#             count+=1
#     return count

# res=fact_Count(10)
# print(res)

# perfect number 

# def perfect(num):
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#             sum+=i
#     return sum
# num=6
# res=perfect(num)
# if num==res:
#     print("perfect")



# def fact(net):
#     if net==1:
#         return net
#     else:
#         return net*fact(net-1)

# def strong(num):
#     temp=num
#     sum=0
#     while temp>0:
#         rem=temp%10
#         fa=fact(rem)
#         sum+=fa
#         temp//=10
#     return sum


# num=145
# res=strong(num)
# if num==res:
#     print("strong")

#  LCM of 2 numbers

# def lcm(num1,num2):
#     pro=num1*num2
#     lcm=max(num1,num2)
#     for i in range(lcm,pro+1):
#         if i%num1==0 and i%num2==0:
#             lcm=i
#             break
#     return lcm
# res=lcm(21,24)
# print(res)


#  printing all fib numbers upto n

# def fib(num):
#     a,b=0,1
#     c=a+b
#     print(a,b , end=" ")
#     while c<=num:
#         print(c , end=" ")
#         a=b
#         b=c
#         c=a+b
# num=10
# res=fib(num)

# def fibChe(num):
#     a,b,c=0,1,1
#     while c<num:
#         a=b
#         b=c
#         c=a+b
#     return c
# num=int(input("Enter a number"))
# print(True if num==fibChe(num) else False)



#  find the 15th tems in the sequence 
# 3,8,13 formula a+(n-1)*d
#  here a=initail number , d=difference 

count=1
net=7
while count<25:
    net+=5
    # sum=net+5
    # net=sum
    count+=1
print(net)
 


a=7
d=5
n=25
sum=a
for i in range(1,n):
    sum+=d
print(sum)


    

    




        







