class Node:
    def __init__(self,key):
        self.right = None
        self.left = None
        self.val = key

def insert(root,node):
    if root is None:
        root.val = node
    else:
        if (root.val > node.val):
            if (root.left is None):
                root.left = node
            else:
                insert(root.left,node)
        else:
            if (root.right is None):
                root.right = node
            else:
                insert(root.right,node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def delete(root,key):
    if not root:
        return root

    else:
        if not root:
            return root
        if root.val > key.val:
            root.left = delete(root.left,key)
        elif root.val < key.val:
            root.right = delete(root.right,key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            temp_val = root.right
            mini_val = temp_val.val
            while temp_val.left:
                temp_val = temp_val.left
                mini_val = temp_val.val
            root.val = mini_val
            right.right = delete(root.right,root.val)
        return root


def min(root):
    while root.right:
        root = root.right
    return(root.val)



            
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80))
inorder(r)
#delete(r,Node(60))
#inorder(r)
print("min",min(r))
