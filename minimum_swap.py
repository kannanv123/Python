A = [1,3,5,4]
B = [1,2,3,7]

for i in range(len(A)-1):
    if A[i] > A[i+1]:
      swap = A[i+1]
      swap_index = i+1

for i in range(len(B)):
    if (B[i] > swap):
         A[swap_index],B[i] = B[i],A[swap_index]        

print(A,B)
