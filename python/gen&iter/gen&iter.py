# genetaor function also called lazy loading functions
#yield is used instead of return
# .__next__() is used to call

# def generator():
#     yield 1
#     yield 2
#     yield 3
# obj=generator()
# # print(obj)
# for i in obj:
#     print(i)
# # print(obj.__next__())




# iterators 
# used to store the list of elements in object
#  iter keyword is used 

# li=[1,2,3]
# it=iter(li)
# # print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# # for i in it:
# #     print(i)


class iterators:
    def __init__(self,mini,maxi):
        self.maxi=maxi
        self.mini=mini
    def written(self):
        values=[]
        for i in range(self.mini,self.maxi):
            values.append(i)
        it=iter(values)
        return it
obj=iterators(1,10)
x=obj.written()
print(x.__next__())
print(x.__next__())



