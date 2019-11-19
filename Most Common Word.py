s = "abcgfhjgk"
s = list(s)
shifts = [3,5,9]
for i in shifts:
    for j in range(shifts.index(i)+1):
          s[j]= (chr(ord(s[j])+ i))
        
print("".join(s))
