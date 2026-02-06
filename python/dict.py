# Dictinory
# it is a collect of data in the form of key value pair which is object data
# keys are immutable and unique
# values can be changed dynamically
# defining the dict:
# d1={}
# d2=dict()
# print(type(d1),type(d2))


# example dictonary
# d1={"Name":"MK","Age":20}
# print(d1)
# d2=dict({"Name":"MK","Age":20})
# print(d2)


# type conversion
#1 list inside list
# d1=dict([["name","MK"],["age",20]])
# print(d1)


# 2 tuple inside list
# d1=dict([("name","MK"),["age",20]])
# print(d1)

#3 tuple inside tuple
# 4 list inside tuple
# 5 key and value parameters as key=value ! key:value

# Accessing dict : can be done by key values 
d1=dict([("name","MK"),["age",20],("Marks",[48,45,40])])
# print(d1["Marks"])
# print(d1)
# print(d1["Marks"][2])

# # by using get method
# print(d1.get("Name")) # if no match then returns none 
# #  get() accepts 2 params get(target_var,default)
# print(d1.get("name"))
# print(d1.get("Name","Key not found"))

# for i in d1:
#     print(i,"=",d1[i])

# Dictonary methods

# update ict value 
d1={"Name":"MK","Age":20}
# d1["Name"]="RK"

# 1 Update method to add new elements

d1.update({"Address":"Nirven"})
# print(d1)

# 2 pop() used to delete elements using keys
# d1.pop("Age")
# print(d1)

#3 clear() used to clear the dict elements from the dict returns emply dict
# d1.clear()
# print(d1)


# 4 key() method returns all the keys of a dict

# print(d1.keys())

# # 5 vaues() returns all the values from the dict
# print(d1.values())

#  6 items() prints keys and values as a list of tuples
# print(d1.items())



# 7 del used to delete the var from memory
# del d1
# print(d1)  NameError: name 'd1' is not defined

# removing methods
 # popitem() used to 
# print(d1.popitem())
# print(d1)

# merging dictionaries
d2={"Phone":7989020757}

# 1 using pipeline operator
# d3=d1|d2
# print(d3)

# 2 using **

# d3={**d1,**d2}
# print(d3)


# fromkey() used to add unique values to different keys
d4={}
d5=d4.fromkeys([1,2,3],"Number")
print(d4)
print(d5)











