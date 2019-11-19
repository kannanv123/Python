arr = [2,3,8,9,12,15,18]
target = 17
i = 0
j = len(arr) -1
while(j > i):
    if(arr[i]+arr[j] == target):
        print(i,j)
        break
    elif(arr[i]+arr[j] > target):
        j-=1
    else:
        i+=1
    
