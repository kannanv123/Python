arr = [2,3,8,9,12,15,18]
target = 17
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if(arr[i] + arr[j] == target):
            print(arr[i],arr[j])
