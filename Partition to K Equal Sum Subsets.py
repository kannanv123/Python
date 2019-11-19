nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
target = sum(nums) /k

list1 = []
if (sum(nums) % k == 0 ):
   for i in nums: 
     remaining = int(abs(i-target))
     if remaining != 0:
       index = nums.index(remaining)
       i2 = nums.pop(index)
       list1.append((i,i2))
     else:
         list1.append(i)
print(list1)
