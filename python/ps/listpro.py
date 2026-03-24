# add element to a list 
list=[1,2,3]
def add_element(num):
    list.append(num)
    return list
a=add_element(4)
print(a)


# remove element in the list 
def remove_element(num):
    if num in list:
        list.remove(num)
    return list
b=remove_element(4)
print(b)


# find maximum number in a list
maxim=list[0]
for i in list:
    if i >maxim:
        maxim=i
print(maxim)



