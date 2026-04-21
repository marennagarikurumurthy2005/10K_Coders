# li=[-7,6,8,2,1,4]
# for i in range(len(li)-1,0,-1):
#     print(li[i])
#     for j in range(0,i):
#         if li[i]<li[j]:
#             li[i],li[j]=li[j],li[i]
# print(li)


li=[-7,6,8,2,1,4]
for i in range(len(li),0,-1):
    for j in range(i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)