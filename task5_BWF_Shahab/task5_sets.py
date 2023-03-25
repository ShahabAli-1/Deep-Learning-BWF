myset = {"Shahab","Ali","Ahmed"}
print(myset)

#=> Union Intersection
set1={'x','z','y'}
set2= {'1','2','y'}

set3 = set1.union(set2)
print(set3)
set3 = set1.intersection(set2)
print(set3)

#=> Difference
set3 = set1.difference(set2)
print(set3)

#=> Symmetric Diff
set3 = set1.symmetric_difference(set2)
print(set3)