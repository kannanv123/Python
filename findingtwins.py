str1 = "abcd"
str2 = "cbad"

if(len(str1) != len(str2)):
    print("not twins")

count = 0
pos1 = 0
pos2 = 0

for i in range(len(str1)):
    if(str1[i] != str2[i]):
        count +=1
        pos1 = pos2
        pos2 = i
        if(count > 2):
            print("they are not twins")

if(count ==2 and str1[pos1] == str2[pos2] and str1[pos2] == str2[pos1]):
    print("they are twins")
