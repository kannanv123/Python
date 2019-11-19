import sys



def ipv4(ip):
 list1 = ip.split("." or ":" or "::")

 if(len(list1) == 4):
    for i in list1:
        if (int(i) > 255):
            return("this is not valid ip")
            sys.exit()
     
    return("this is a valid ipv4 address")    


def ipv6(ip):
 list1 = ip.split(":" or ":" or "::")
 if(len(list1) <= 8):
    for i in list1:
        for letter in i:
            if letter not in "1234567890abcdefABCDEF":
              return("this is not valid ip")
              sys.exit()
     
 return("this is a valid ipv6 address")   


ip = input("enter the ip")
if(ip.find(".") > 0):
  print(ipv4(ip))
elif(ip.find(":") > 0):
   print(ipv6(ip))
else:
   print("neither ipv4 nor ipv6")
            
