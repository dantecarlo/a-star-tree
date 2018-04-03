import math

class Node():

  def __init__(self,key,cost=0,parent=None,distance=0):
    self.key = key
    self.distance = distance
    self.cost = cost
    self.children = []

    self.left = None
    self.right = None

    self.parent = parent

  def __repr__(self):
    return ("NODE content is:  key:{}, children:{}, parent:{}\n".format(self.key, self.children, None if self.parent is None else self.parent.key)) 
    

class Tree():

  def __init__(self):
    self.root = None    
    

  def search(self,key,node=None,cont=0):

    if node is None:
      node = self.root

    if self.root.key == key:
      print("Found")
      return self.root
    
    if node.key == key:
        print("Found")
        return node

    elif cont < len(node.children):
      if key == node.children[cont].key:
        print("Found")
        return node
      return self.search(key,node,cont+1)              
              
    else:
        print("Not found")
        return None
      


  def add_node(self,key,key2=None,node=None,cost=0):

    if node is None:
      node = self.root
    
    if self.root is None:
      self.root = Node(key)
      print("Added")

    else:
      if self.search(key,node) is None:
        print("Key not found, nothing done")
        return False
      else:
        node = self.search(key,node)
        distance = math.sqrt((key2[0]-key[0])**2+(key2[1]-key[1])**2)
        node.children.append(Node(key2,cost,node,distance))
        print("Added")
        return True
  
  

  def delete_node(self,key,node=None):
    #search for the node to be deleted in tree
    if node is None:
      node = self.search(key)#return the node to be deleted

    #root has no parent node  
    if self.root.key == node.key: #if it is root
      parent_node = self.root
    else:
      parent_node = node.parent
      

    '''case 1: The node has no chidren'''
    if node.left is None and node.right is None:
      if key <= parent_node.key:
        parent_node.left = None
      else:
        parent_node.right = None
      return

    '''case 2: The node has children'''
    ''' if it has a single left node'''
    if node.left is not None and node.right is None :
      if node.left.key < parent_node.key : 
        parent_node.left = node.left
      else:
        parent_node.right = node.left

      return

    '''if it has a single right node'''
    if node.right is not None and node.left is None:
      if node.key <= parent_node.key:
        parent_node.left = node.right
      else:
        parent_node.right = node.right
      return

    '''if it has two children'''
    '''find the node with the minimum value from the right subtree.
       copy its value to thhe node which needs to be removed.
       right subtree now has a duplicate and so remove it.'''
    if node.left is not None and node.right is not None:
      min_value = self.find_minimum(node)
      node.key = min_value.key
      min_value.parent.left = None
      return


  def find_minimum(self,node = None):
    
    if node is None:
      node = self.root

    '''find mimimum value from the right subtree'''
    
    '''case when there is only a root node'''
    if node.right is not None:
      node = node.right
    else:
      return node

    if node.left is not None:
      return self.find_minimum(node = node.left)
    else:
      return node

  def tree_data(self,node=None):
    if node is None:
      node = self.root

    stack = []
    while stack or node:
      if node is not None:
        stack.append(node)
        node = node.left
      else:
        node = stack.pop()
        yield node.key
        node = node.right



    
      
t=Tree()
t.add_node([3,1])



t.add_node([3,1],[2,2])
t.add_node([3,1],[1,2])
t.add_node([1,2],[0,0])

t.search([0,0])




'''
t.add_node(13)
t.add_node(14)
t.add_node(8)
t.add_node(9)
t.add_node(7)
t.add_node(11)
'''
