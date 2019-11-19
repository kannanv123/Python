import collections
a = [1,2,3,4,4,5,5,6,1]

print([item for item in collections.Counter(a).items() if count > 1])
