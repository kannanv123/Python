input1 = [3,1,2,4,5]
sum1 = 0 
k = len(input1)
for i in range(1,len(input1)+1):
    j = 0
    while(j < k):
        sum1+= min(input1[j:j+i])
        j+=1
    k-=1
print(sum1)
