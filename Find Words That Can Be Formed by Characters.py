words = ["hello","world","leetcode"]
chars = "welldonehoneyr"

length = 0
for i in words:
 for j in i:
   if j not in chars:
     break
 else:
  length+=len(i)

print(length)
~               
