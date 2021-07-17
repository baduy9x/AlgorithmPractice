def get_cheapest_cost(rootNode):
  
  result = float("inf")
  stack = []
  stack.append((rootNode, rootNode.cost))
  seen = set()
  seen.add(rootNode)
  
  while stack:
    current_node, path_sum = stack.pop()
    if len(current_node.children) == 0:
      if path_sum < result:
        result = path_sum
    else:
      for child in current_node.children:
        if child not in seen and path_sum + child.cost <= result:
          stack.append((child, path_sum + child.cost))
          seen.add(child)
  return result

########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None
 

if __name__ == '__main__':
  root = Node(0)
  
  one = Node(5)
  two = Node(3)
  three = Node(6)
  
  four = Node(4)
  five = Node(2)
  six = Node(0)
  seven = Node(1)
  eight = Node(5)
  
  nine = Node(1)
  ten = Node(10)
  eleven = Node(1)
  
  
  
  root.children.extend([one, two, three])
  one.children.append(four)
  two.children.extend([five, six])
  three.children.extend([seven, eight])
  
  five.children.append(nine)
  six.children.append(ten)
  
  nine.children.append(eleven)
  
  print(get_cheapest_cost(root))
  