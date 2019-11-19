input1 = ["a","b","ba","bca","bda","bdca","bdeca"]

count = 1
word1 = input1[0]
i =1
while i < len(input1):
    word2 = input1[i]
    if ( len(word1) < len(word2)):
       for j in word1:
           if (j not in word2):
               i+=1
               break
       else:
           count +=1
           word1 = word2
           i+=1
    else:
        i+=1
        

print(count)
