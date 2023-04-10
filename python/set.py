set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {2,4,6,8,10,12}
set3 = {2,6}

print(set1)
set1.add(14)
print(set1.difference(set2))
print(set1.intersection(set2))
print(set3.issubset(set1))
print(set2.issubset(set1))
set4= set2.copy()
set1.discard(10)
print(set1)
set1.add(10)
print(set1.union(set3))




