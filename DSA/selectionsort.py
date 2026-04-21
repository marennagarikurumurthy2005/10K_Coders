
li=[-7,6,8,2,1,4]
for i in range(len(li)):
    m=i
    for j in range(i+1,len(li)):
        if li[j]<li[m]:
            m=j
    
    li[m],li[i]=li[i],li[m]

print(li)
    