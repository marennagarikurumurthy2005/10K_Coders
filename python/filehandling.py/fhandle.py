# f=open("file1.txt","r")
# # f.write("This is kurumurthy marennagari")
# if f.readable():
#     # print("readable")
#     for i in f.read():
#         if i in "aeiouAEIOU":
#             print(i)
# else:
#     print("file is not readable")
# f.close()


# f=open("file1.txt","r")
# if f.readable():
#     for i in f.read():
#         if i in "0123456789":
#             print(i)
# f.close()  



# f=open("file1.txt","r")
# # f.write("This is kurumurthy marennagari")
# if f.readable():
#     # print("readable")
#     for i in f.read():
#         if i in "aeiouAEIOU":
#             print(i.upper())
# else:
#     print("file is not readable")
# f.close()


# f=open("file1.txt","r")
# if f.readable():
#     sum=0
#     for i in f.read():
#         sum+=ord(i)
#         # print(ord(i))
# print(sum)
# f.close()

# f=open("file1.txt","r")
# if f.readable():
#     for i in f.read():
#         if i!=" ":
#             print(i,end="")
       
# f.close()


#binary file

#file handling with "with keyword"

# 1 odd apend


# l1=[1,8,6,3,7,5,45,85,69,86,24,40]
# with open("with.txt","+a") as f:
#     if f.writable():
#          f.write("even")
#         for i in l1:
#             if i%2==0:
#                 f.write(f"{i}\n")

# with open("with.txt","+a") as f:
#     if f.writable():
#         f.write("prime numbers from 1 to 20 \n")
#         for i in range(1,20):
#             flag=0
#             for j in range(2,i):
#                 if i%j==0:
#                     flag=1
#                     break
#             if flag==0:
#                 f.write(f"{i} ")


# l1=["murthy","asap","name","apple"]
# with open("with.txt","+a") as f:
#     if f.writable():
#         f.write("\n")
#         f.write("names starts with a \n")
#         for i in l1:
#             if i[0] in "aA":
#                 f.write(f"{i} ")


l1=["murthy","asap","name","apple"]
with open("with.txt","+a") as f:
    if f.writable():
        f.write("\n")
        f.write("names with len >5 \n")
        for i in l1:
            if len(i)>5:
                f.write(f"{i} ")





