input1 = [3,2,1,2,1,7]

sort = sorted(input1)

for i in range(len(input1)-1):
    if ( sort[i] == sort[i+1]):
        temp = sort[i+1]
        while (temp in sort):
            temp +=1
        sort[i+1] = temp
print(sum(sort)- sum(input1))
