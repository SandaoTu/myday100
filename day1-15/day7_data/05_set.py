#集合的交集、并集、差集

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7,8}

#交集
print(set1&set2)
print(set1.intersection(set2))

#并集
print(set1|set2)
print(set1.union(set2))

#差集
print(set1 - set2)
print(set2 - set1)
print(set1.difference(set2))
print(set2.difference(set1))

#
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
