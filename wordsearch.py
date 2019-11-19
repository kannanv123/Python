from collections import defaultdict
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

d = defaultdict(float)
for k in board:
    for s in k:
        d[s] +=1

print(d)

word = 'SSFCDEE'
e = defaultdict(float)
for char in word:
    e[char] += 1

print(e)
for key in e:
   output = 'true' 
   if e[key] > d[key]:
     output = 'False'
     break

print(output)
     
