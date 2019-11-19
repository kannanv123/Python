text = "antaprezatepzapreanta"
i = 0
j = len(text)-1
word1 = text[i]
word2 = text[j]
count = 0
while (j > i):
    if (word1 == word2):
        count +=2
        word1 = text[i+1:i+2]
        word2 = text[j-1:j]
        j-=1
        i+=1
    else:
        word1 += text[i+1]
        word2 = text[j-1] + word2
        j-=1
        i+=1
count+=1

print(count)

