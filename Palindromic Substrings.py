input1 = "aaabccba"
k = len(input1)
list1 = []
for i in range(1,len(input1)+1):
    j = 0
    while(j < k):
        string = input1[j:j+i]
        if (string == string[::-1]):
          list1.append(string)  

        j+=1
    k-=1
print(list1)
