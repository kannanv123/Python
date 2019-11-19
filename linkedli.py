class Node:
    def __init__(self,data):
        self.data = data
        self.head = None

class linkedlist:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev 
llist = linkedlist() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 
  
#print "Given Linked List"
llist.printlist()
print("\n")
llist.reverse() 
#print "\nReversed Linked List"
llist.printlist() 
        
