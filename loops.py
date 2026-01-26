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


i=int(input())
count=0
if i<10:
    count+=1
else:
    while i>0:
        count+=1
        i//=10
print(count)

