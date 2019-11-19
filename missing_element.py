a = [5,1,5,2,5,3,5,4]
b = set(a)
word = (sum(a)-sum(b))/(len(a)-len(b))
print(int(word))


