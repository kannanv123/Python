input1 = input("enter the strings")
words = input1.split(" ")
length = len(words)
str1 =""
while (length > 0):
   str1 = str1 + " " +words[length-1]
   length-=1
print(str1[1:])
