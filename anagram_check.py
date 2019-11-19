from collections import defaultdict
s = "clint eastwood"
t = "old west action"

s = s.replace(" ","")
t = t.replace(" ","")

s_count = defaultdict(int)
t_count = defaultdict(int)

for i in s:
  s_count[i] += 1

for i in t:
  t_count[i] +=1


for key,value in s_count.items():
    if(key not in t_count.keys()):
       print("it is not an anagram")
       break

    if(value != t_count[key]):
      print("it is not an anagram")
      break

else:
  print("it is an anagram")

  
