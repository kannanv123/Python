a = int(input("enter the number"))
if a > 1:
  for j in range(2,a+1):  
    for i in range(2,j):
        if (j%i == 0):
            break
    else:
        print(j,"it is a palindrome")
else:
    print("its a palindrome")
            


