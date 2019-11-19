num_of_people = 4
list1 = [0]*num_of_people
j = 0
candies = 7
k = 1
while candies:
        if(j == num_of_people):
          j = 0
        if(candies >= k):
          list1[j] += k
          candies -=k
          
        else:
            list1[j] += candies
            candies =0
        k+=1
        j+=1
        
print(list1)
