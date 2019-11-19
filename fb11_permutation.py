num = input("enter the input")
str1 ="abcdefghijklmnopqrstuvwxyz"
count = 0
for i in num:
    a = int(i) 
    if (a < 26):
        print(str1[a-1])
        count+=1
        if count != len(num):
         b = int(i + num[count])
         if (b < 26):
            print(str1[b-1])
