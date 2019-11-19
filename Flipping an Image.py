nums = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
list1 = []

for num in nums:
    num = num[::-1]
    for i in range(len(num)):
        num[i] = 1 - num[i]
    list1.append(num)

print(list1)
        
