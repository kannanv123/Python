def binary_search(arr,x,l,r):
    while l <= r:
        mid = l + (r-1)/2
        if ( arr [int(mid)] == x):
            print("True")

        elif ( arr[int(mid)] > x ) :
            l = mid +1

        else:
            r = mid -1




arr = [1,3,5,7,8]
x = 7
binary_search(arr,x,0,len(arr)-1)
