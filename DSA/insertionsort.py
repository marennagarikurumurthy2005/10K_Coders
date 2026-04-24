# li=[0,2,4,8,-9,9,6,-1,-6]
# for i in range(1,len(li)):
#     key=li[i]
#     index=i-1
#     while key<li[index] and index>=0:
#         li[i],li[index]=li[index],li[i]
#         index-=1
#         i-=1
# print(li)

li=[-10,0,2,1,4,8,-9,9,6,-1,-6]
for i in range(1,len(li)):
    key=li[i]
    index=i-1
    while index>=0 and key<li[index]:
        li[index+1]=li[index]
        index-=1
    li[index+1]=key
print(li)     



""" exam day1 """
    