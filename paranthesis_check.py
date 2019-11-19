open_list = ["[","{","("] 
close_list = ["]","}",")"]

mystr = '{[]{()}'
stack = []

for i in mystr:
  if i in open_list:
    stack.append(i)
  elif i in close_list:
     pos = close_list.index(i)
     if (len(stack) > 0 and (open_list[pos] == stack[len(stack)-1])):
        stack.pop()
     else:
       print("it is unbalanced")

if (len(stack) == 0 ):
  print("it is balanced")
