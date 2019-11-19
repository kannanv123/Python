array1 = [1,2,3,4,5]
array2 = [2,3,5,7]
list1 = []
i = 0
j = 0
m = len(array1)
n = len(array2)

while (i < m and j <n ):
  if (array1[i] < array2[j]):
     i+=1
  elif(array2[j] < array1[i]):
       j +=1
  else:
       list1.append(array1[i])
       i+=1
       j+=1


print(list1)
                          
