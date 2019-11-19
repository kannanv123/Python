def maximum(arr):
  maximum = summ = arr[0]
  for i in range(1,len(arr)): 
    summ =  summ + arr[i]
    if(summ > 0):
       maximum = max(summ , maximum)
    else:
      summ = 0
  return maximum

print(maximum([11, -12, 15, -3, 8, -9, 1, 8, 10, -2]))
