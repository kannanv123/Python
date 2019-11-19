/*def anagram(s, t):
   s = s.replace(" ","")
   t = t.replace(" ","")
   counter = {}
   if (len(s)!= len(t)):
       return False
   for letter in s:
       if letter in counter:
           counter[letter] += 1
       else:
           counter[letter] = 1
   for letter in t:
       if letter in counter:
           counter[letter] -= 1
       else:
           return False
   print(counter)
   for key,values in counter.items():
       if (values != 0):
           return False
   return True
   Pass
   
print(anagram('do g', 'god')) */


