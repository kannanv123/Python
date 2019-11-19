from collections import defaultdict
number = '12323790'

magic_flag = True
for i in range(1,7):
    if (str(i) not in number):
        magic_flag = False

count = defaultdict(int)

for i in number:
    count[i] += 1

for keys,value in count.items():
   if (value >= 3):
       magic_flag = True

k = 0
l = 0
for i in range(len(number)-1):  
  if (k != 2 and l != 2) :
    if (int(number[i]) == int(number[i+1])+1):
        k +=1
    else:
        k = 0
    if(int(number[i]) == int(number[i+1])-1):
        l +=1
    else:
        l = 0
  else:
      magic_flag = True
      break

if(magic_flag == True):
    print("It is magic number")

else:
    print("It is not magic number")
