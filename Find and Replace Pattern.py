words =["abc","deq","mee","aqq","dkd","ccc"]
pattern = "bab"

res = []
for word in words:
    dict1 = {}
    dict2 = {}
    match = True
    for i in range(len(word)):
        if(word[i] not in dict1):
            dict1[word[i]] = pattern[i]
        else:
            if(dict1[word[i]] != pattern[i]):
              match = False
              break
        if(pattern[i] not in dict2):
            dict2[pattern[i]] = word[i]
        else:
            if(dict2[pattern[i]] != word[i]):
              match = False
              break
    if match:
        res.append(word)

print(res)
        
              
              
