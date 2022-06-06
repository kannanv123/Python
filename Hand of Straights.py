hand = [1,2,3,6,2,3,4,7,8]
w = 3
j= 0
list2 = []
if len(hand)%3 != 0:
 print("can't be formed")

else:
 while (j < len(hand)):
  list1 = hand[j:j+w]
  j =j+w
  list2.append(list1)

print(list2)
