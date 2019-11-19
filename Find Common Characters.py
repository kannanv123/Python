A= ["bella","labeal","rollear"]
result = []
N = len(A)
for i in A[0]:
  for j in range(1,N):
      if i not in A[j]:
          break
  else:
      result.append(i)

print(result)
      
   
