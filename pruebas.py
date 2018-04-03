# Build an N-Tree from 2D array of Parent-Child pairs

import logging
from collections import deque

"""
   TREE:
            3
          / | \
        4   5  6
           / \
          7   8
         /
        9
        
    ALGO:
       - ASSOCIATIVE MAP; ACCUMULATING EDGEs per Parent node!
       - LOOKUP PARENT to ACCUMULATE CHILDREN for PARENT at ANY Level!
       - WALK up from ANY EDGE to LOOKUP PARENT where Node.Parent == None
         to find GLOBAL ROOT of tree
       - DEPTH-WALK is similar; and O(logN)
"""

class Node:

    # ATTN:
    # - remember __ for ctor
    # - remember self
    # - OK to just reference self elements for declaration
    def __init__(self, key, parent = None):
        self.key = key
        # ATTN:  multiple children
        self.children = []
        self.parent = parent
      
    # ATTN:  override for logging contnents!  
    # https://stackoverflow.com/questions/44342081/correct-way-to-write-repr-function-with-inheritance
    # RECALL for toString()
    # ATTN:  Python 1-line conditional assignment!
    # TODO: PYTHON for getting List of keys only from children nodes list using list comp
    def __repr__(self):
      return ("NODE content is:  key:{}, children:{}, parent:{}\n".format(self.key, self.children, None if self.parent is None else self.parent.key))
        
# PUNT:  SIMPLISTIC INTEGER KEY to ACCUM/MAP PARENT at EACH Level to LIST of children 
#         eg 3 has children 4,5,6
#         TRICK:  accum Dict with value of LIST; LOOKUP by INTEGER key value
def buildTreeV1(data):

  accumTree = {}
  for edge in data:
    print(edge)
    if (edge[0] in accumTree):
      accumTree[edge[0]].append(edge[1])
    else:
      accumTree[edge[0]] = [ edge[1], ]
      
  print("BUILT TREE IS:  ")    
  print(accumTree)
  
  return None
          
# ITER2
# Load ALL NODES indexed by KEY to support LOOKUP
# Edges can be specified in ANY ORDER, 
# NEEDs to ESTABLISH BOTH endpoints to capture DIRECTIONAL LOOKUP
# to EITHER PARENT or CHILD!
def buildTreeV2(data):
  
  accumTree = {}
  
  # TRICK1:  CONSTRUCT and KEY-INDEX NODE to support LATER LINK LOOKUPS!  NOT doing LINKs yet!
  for edge in data:
    accumTree[edge[0]] = Node(edge[0])
    accumTree[edge[1]] = Node(edge[1])
  
  # TRICK2: 
  for edge in data:
    # ATTENTION!  need to append NODE via LOOKUP to prior-populated KEY => NODE map!
    if accumTree[edge[0]] is None:
      accumTree[edge[0]].children = [ accumTree[edge[1]], ]
    else:
      accumTree[edge[0]].children.append( accumTree[edge[1]] )
    # TRACK PARENT in OTHER direction for EACH child!
    accumTree[edge[1]].parent = accumTree[edge[0]]
    
  return accumTree
  
def findGlobalRoot(accumTree):
  # find the GLOBAL ROOT; THEN walk down the tree
  allNodes = accumTree.values()
  # print(allNodes)
  
  # TRICK3:  FILTER trick, and Python3 needs to materialize LIST
  globalRootList = list(filter(lambda x: (x.parent is None), allNodes))
  # print("TYPE IS:  ")
  # print(type(globalRootList))
  # print("CONTENT IS:  ")
  # print(globalRootList)
  globalRoot = globalRootList[0]
  # print(type(globalRoot))
  # print("GLOBAL ROOT KEY IS:")
  # print(globalRoot.key)
  return globalRoot

# ATTN:  use deque as efficient for removing from FRONT of Q
def traverseBFS(accumTree):
  
  globalRoot = findGlobalRoot(accumTree)
  
  # TRICK4:  Use deque as more efficient than List for Q in Python!
  bfsQ = deque()
  bfsQ.append(globalRoot)
  while bfsQ:
    currNode = bfsQ.popleft()
    print (currNode.key)
    nextChildren = currNode.children
    bfsQ.extend(nextChildren)
    
# ATTN:  OK to use List as stack as insert-removal from SAME-SIDE!
#        OTHERWISE, use deque
def traverseDFS(node):

  # nonsense case, exit
  if (node is None):
    return
  
  # testing for LEAF to print at MAX DEPTH; EXIT condition
  if not node.children:
    print(node.key)
  else:
    for child in node.children:
        traverseDFS(child)
    # print current value AFTER RECURSE to depth
    print(node.key)
    
    
# **************** DRIVER to test tree build with EXCEPTION-HANDLING!  ***************
try:

  """
  print("TEST1:  Load 1-Edge Tree, Level 0, 1")
  testData1 = [[1,2]]
  print "INPUT IS:  \n{}".format(testData1)
  rootTree1 = buildTree(testData1)
  print(rootTree1)
  """
  
  """
  print("TEST2:  Load LEVEL1 of 3-Edge Tree")
  testData2  = [[3,6], [3,4], [3,5]]
  print("INPUT IS:  \n{}".format(testData2))
  rootTree2 = buildTreeV2(testData2)
  print("\n*** BUILT TREE DICT IS:  ")
  print(rootTree2)
  """

  # ATTN:  PRINT gets CONFUSING AFTER MULTI-LEVELS due to NESTED DEPTH content!
  #        SO, need function AROUND printing CHILDREN that sets MAX-DEPTH!
  """
  print("TEST3:  Load LEVEL2 of N-Edge tree")
  testData3  = [[5,7], [3,6], [3,4], [5,8], [3,5]]
  print("INPUT IS:  \n{}".format(testData3))
  rootTree3 = buildTreeV2(testData3)
  print("\n*** BUILT TREE DICT IS:  ")
  print(rootTree3)
  """
  
  print("TEST4:  Load LEVEL3 of N-Edge tree")
  testData3  = [[5,7], [3,6], [3,4], [5,8], [3,5], [7,9]]
  print("INPUT IS:  \n{}".format(testData3))
  rootTree3 = buildTreeV2(testData3)
  print("\n*** BUILT TREE DICT IS:  ")
  print(rootTree3)
  
  print("\n*** BFS TRAVERSAL OF TREE IS:  ")
  traverseBFS(rootTree3)
  
  print("\n*** DFS TRAVERSAL OF TREE IS:  ")
  globalRoot = findGlobalRoot(rootTree3)
  traverseDFS(globalRoot)
  
except Exception as ex:

  print(ex)
  # TODO:  repl.it doesn't show this in output!
  logging.exception(ex)