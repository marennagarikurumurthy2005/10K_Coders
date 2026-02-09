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

def table(num):
    for i in range(1,num+1):
        print(f"{i} Multiplication Table-------------------")
        print("")
        for j in range(1,11):
            print(f"{i} X {j} = {i*j}")
        


table(10)


