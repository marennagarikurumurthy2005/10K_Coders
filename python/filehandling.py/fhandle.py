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


f=open("file1.txt","r")
if f.readable():
    sum=0
    for i in f.read():
        sum+=ord(i)
        # print(ord(i))
print(sum)
f.close()

f=open("file1.txt","r")
if f.readable():
    for i in f.read():
        if i!=" ":
            print(i,end="")
       
f.close()

