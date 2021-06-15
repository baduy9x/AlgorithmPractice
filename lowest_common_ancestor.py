class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    from collections import defaultdict, deque

    father = {}
    father[root.info] = None

    queue = deque()
    queue.append(root)
    
    while queue:
        node = queue.popleft()
        if node.left is not None:
            queue.append(node.left)
            father[node.left.info] = node
        if node.right is not None:
            queue.append(node.right)
            father[node.right.info] = node

        if v1 in father and v2 in father:
            break
    
    ancestor_v1 = set()
    v1_ = v1
    while v1_ in father and father[v1_] is not None:
        ancestor_v1.add(father[v1_].info)
        v1_ = father[v1_].info
    
    ancestor_v2 = set()
    v2_ = v2
    while v2_ in father and father[v2_] is not None:
        ancestor_v2.add(father[v2_].info)
        v2_ = father[v2_].info


    while v2 in father:
        current_node = father[v2]
        if current_node is not None and current_node.info == v1:
            return current_node

        if current_node is not None and current_node.info in ancestor_v1:
            return current_node
        v2 = father[v2].info

    while v1 in father:
        current_node = father[v1]
        if current_node is not None and current_node.info == v2:
            return current_node

        if current_node is not None and current_node.info in ancestor_v2:
            return current_node
        v1 = father[v1].info
