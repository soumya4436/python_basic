myset={1,5.583,"set","set",True} # unorder, unindex,unchangeable
print(myset)
for i in myset:
    print(i)
myset.add("item")
print(myset)
myset.remove("item")
print(myset)
# union function
set1={1,2,3,4}
set2={5,6,7,8,9}
print(set1.union(set2))