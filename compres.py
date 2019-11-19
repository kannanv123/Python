def compress(s):
    r=""
    i =0
    l = len(s)
    counter = 1
    if (l == 0):
        return("")
    elif(l == 1):
        return( s +"1")
    else:
        while i < l-1 :
         if (s[i] == s[i+1]):
           counter += 1
         else:
             r = r+s[i]+ str(counter)
             counter =1
         i += 1
        r = r + s[i] + str(counter) 
        return r 

print(compress('ABBBBCCCCDDEA'))
