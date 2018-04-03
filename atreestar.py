import math

class Node():

  def __init__(self,key,cost=0,parent=None,distance=0):
    self.key = key
    self.distance = distance
    self.cost = cost
    self.children = []
    self.parent = parent

  def __repr__(self):
    return ("NODE:key:{}, children:{}, parent:{} |\n".format(self.key, self.children, None if self.parent is None else self.parent.key)) 
    

class Tree():

  def __init__(self):
    self.root = None    
    



  def search(self,key,node=None):

    if node is None:
      node = self.root


    if node.key == key:
        #print("Found")
        return node

    else: 
      for child in node.children:
        #print("In")
        self.search(key,child)


  def add_node(self,key,key2=None,node=None,cost=0):
    #print("add")
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
        #print(node)
        distance = math.sqrt((key2[0]-key[0])**2+(key2[1]-key[1])**2)
        node.children.append(Node(key2,cost,node,distance))
        print("Added")
        return True
  
  



  def tree_data(self,node=None,stack=[]):


    if node is None:
      node = self.root

    stack.append(node.key)
    for child in node.children:
        self.tree_data(child,stack)            
        
    return stack



    
      
t=Tree()
t.add_node([3,1])



t.add_node([3,1],[2,2])
t.add_node([3,1],[1,2])
t.add_node([1,2],[0,0])

print(t.search([0,0]))

print(t.tree_data())
#print("data")
#print(t.tree_data())
