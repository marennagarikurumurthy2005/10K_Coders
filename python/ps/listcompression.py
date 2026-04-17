# l1=[i%2==0 for i in range(20)]
# print(l1)


print([i for i in range(20) if i%2==0])

print([i for i in ["name","rollnum"] if "a" in i])

print([i for i in [1,-4,-2,-6,7,4,10] if i<0])

print([i for i in range(1,11)])

print([x.upper() for x in ["mk","qk"]])

print([x  for x in "kurumurthy" if x in "aeiou"])

print([i if i>0 else 0 for i in [0,2,3,-8,6]])

print([len(x) for x in ["murthy","velura"]])

print([x for x in [1,28,6,7,66,9,3,82,63,74,45,8] if x%2==0 and x%3==0])

print("dummy")