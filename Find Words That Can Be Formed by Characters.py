from collections import Counter
words = ["ccat","bt","hat","tree"]
chars = "atach"
length = 0
for word in words:
    if not (Counter(word) - Counter (chars)):
            print(word)
print(length)


    
