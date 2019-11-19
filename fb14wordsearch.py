board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
dict1 ={}
for i in board:
  for j in i:
      if (j in dict1.keys()):
          dict1[j]+=1
      else:
          dict1[j] =1

print(dict1)
