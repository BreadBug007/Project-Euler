# -*- coding: utf-8 -*-


import time

start = time.time()

class Node:

    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val        

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)  

def deleteNode(root, node): 
  
    # Base Case 
    if root is None: 
        return root  
  
    # If the key to be deleted is smaller than the root's 
    # key then it lies in  left subtree 
    if node.data < root.data: 
        root.l_child = deleteNode(root.l_child, node) 
  
    # If the kye to be delete is greater than the root's key 
    # then it lies in right subtree 
    #elif(node.data > root.data): 
       # root.r_child = deleteNode(root.r_child, node) 

def pre_order_print(root):
    if not root:
        return
    print(root.data)
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)
    
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i) 
        
def printGivenLevel(root , level):    
    if root is None:        
        return    
    if level == 1:        
        print(root.data)    
    elif level > 1 :        
        printGivenLevel(root.l_child , level-1)        
        printGivenLevel(root.r_child , level-1) 
        
def height(node):    
    if node is None:        
        return 0    
    else :        
        # Compute the height of each subtree          
        lheight = height(node.l_child)        
        rheight = height(node.r_child)          
        #Use the larger one        
        if lheight > rheight :            
            return lheight+1        
        else:            
            return rheight+1 
        
l = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

l = l.split(" ")
l = [int(i) for i in l]
r = Node(l[0])
for i in l[1::]:
    binary_insert(r, Node(i)) 
for i in l[1::]:
    deleteNode(r, Node(i))
    

pre_order_print(r)


end = time.time()

print(l, end-start)
