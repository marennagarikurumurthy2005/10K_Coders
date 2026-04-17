# list=[10,15,60,3,45,8]
# largest=list[0]
# sec_largest=list[0]
# for i in list:
#     if i>largest:
#         sec_largest=largest
#         largest=i
#     elif i>sec_largest and i!=largest:
#         sec_largest=i
# print(sec_largest)

# list=[10,5,6,3,45,8]
# l=len(list)
# for i in range(l//2):
#     list[i],list[l-1]=list[l-1],list[i]
#     l-=1
# print(list)


# list=[0,10,20,0,5,0,54,5,6]
# p=0
# l=len(list)
# for i in list:
#     if i!=0:
#         list[p]=i
#         p+=1

# while p<l:
#     list.append(0)
#     p+=1
# print(list)


list=[4,5,7,2,6,9,0,3]
target=9
res=[]
l=len(list)
for i in range(l):
    for j in range(i+1,l):
        if list[i]+list[j]==target:
            res.append([i,j])
print(res)
            






    