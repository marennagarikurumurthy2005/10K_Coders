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
print(d1["Marks"])
print(d1)
print(d1["Marks"][2])

# by using get method
print(d1.get("Name")) # if no match then returns none 
#  get() accepts 2 params get(target_var,default)
print(d1.get("name"))
print(d1.get("Name","Key not found"))





