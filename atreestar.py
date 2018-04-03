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
    return ("NODE:key:{}, children:{}, parent:{} |\n".format(self.key, self.children, None if self.parent is None else self.parent.key)) 
    

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
        print(node)
        distance = math.sqrt((key2[0]-key[0])**2+(key2[1]-key[1])**2)
        node.children.append(Node(key2,cost,node,distance))
        print("Added")
        return True
  
  



  def tree_data(self,node=None,cont=0,stack=[]):


    if node is None:
      node = self.root

    stack.append(node.key)
    print(len(node.children))
    if cont < len(node.children):
      print("IN")
      #print(len(node.children))
      #stack.append(node.children[cont].key)
      return self.tree_data(node.children[cont],cont+1,stack)              
              
    
    return stack



    
      
t=Tree()
t.add_node([3,1])



t.add_node([3,1],[2,2])
t.add_node([3,1],[1,2])
t.add_node([1,2],[0,0])

t.search([0,0])
print("data")
print(t.tree_data())




'''
t.add_node(13)
t.add_node(14)
t.add_node(8)
t.add_node(9)
t.add_node(7)
t.add_node(11)
'''
