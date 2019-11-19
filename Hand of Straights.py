hand = [1,2,3,6,2,3,4,7,8]
w = 3

if (len(hand)%w != 0):
    print("False")
i = 0
key = hand[i]
while (i < len(hand)-1):
    if (key > hand[i+1]):
        key = hand[i]
        while key > hand[i+1]:
            hand[i] = hand[i+1]
            i+=1
        hand[i] = key

    else:
       key = hand[i+1] 
       i+=1 
print(hand)
