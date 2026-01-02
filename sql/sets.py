#sets
# it is a collection of homogeneous and heterogeneous data
# denoted with {}
# won't allows the duplicate
# unordered data type i.e printing order will be chnaged and no particular index is given to any element
# set creating
# s1={1,5,6}
# print(s1)
# print(type(s1))

# s2=set() # empy set should only declared with set() constructor 
# print(type(s2)) # creating set like this {} will converted to dict data type

# Homo data
s1={1,5,6}

# hetero data
s2={"Kurumurthy",1,5} # the elements of set must be immutable i.e cant be changed
print(s1)
print(s2)

# set methods
# add() used to add elements into the set
# syntax : var.add(single_element)

s2.add("MK")
s2.add(6)
print(s2)

# update() used to add multiple elements
# syntax var.update(multiple_elements) 
s2.update("RK")
print(s2)
# {1, 'Kurumurthy', 5, 6, 'MK'}
# {1, 'Kurumurthy', 5, 6, 'K', 'R', 'MK'}

# updating with list,set and tuples

s2.update(["RK",75])
s2.update({"MG",95})
s2.update(("AS",73))
 # use tuple vicely
print(s2)

# pop method used to pop random element as set won't has indexes
# clear used to delete all the elements from set 
# remove used to delete exact element 
s2.remove("AS")
print(s2)
# element not found then throws error as key error 
# discard  same as remove but it does not return error if elements not found
