arr = [3,2,1,5,2,3,4]

for i in range(len(arr)):
    if (arr[abs(arr[i])] > 0):
       arr[abs(arr[i])] = - arr[abs(arr[i])]

    else:
        print(abs(arr[i]))
        
    
