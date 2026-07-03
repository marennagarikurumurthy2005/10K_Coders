

# def primecheck(sup):
#     for i in range(2,sup):
#         if sup%i==0:
#             return False
#     else:
#         return True

# n=1000
# lf=n-1
# rg=n+1
# c=0
# while True:
#     if primecheck(lf)==0:
#         lf-=1
#     else:
#         c+=1
#     if primecheck(rg)==0:
#         rg+=1
#     else:
#         c+=1
#     if c==2:
#         break
# print(lf,n,rg)



#LCM
n=24
m=30
for i in range(max(m,n),m*n+1):
    if i%m==0 and i%n==0:
        print(i)
        break

# HCF / GCD

for i in range(min(n,m),0,-1):
    if n%i==0 and m%i==0:
        print(i)
        break


        




