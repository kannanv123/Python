str1 = "ha2c2h3"
length = ''
for i in str1:
    if (i.isdigit()):
        length*= int(i)
    elif (i.isalpha()):
        length+=i
    else:
        continue

print(length)
