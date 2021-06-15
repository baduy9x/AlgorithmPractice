from collections import deque
import sys

# sys.stdin = open("input.txt", "r")

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
    
    def get_height(self):
        queue = deque()
        queue.append((self.root, 0))
        height = 0
        while queue:
            node, current_level = queue.popleft()
            if node.left is None and node.right is None:
                if current_level > height:
                    height = current_level

            if node.left is not None:
                queue.append((node.left, current_level + 1))       
            if node.right is not None:
                queue.append((node.right, current_level + 1))
        return height

def height(root):
    queue = deque()
    queue.append((root, 0))
    height = 0
    while queue:
        node, current_level = queue.popleft()
        if node.left is None and node.right is None:
            if current_level > height:
                height = current_level

        if node.left is not None:
            queue.append((node.left, current_level + 1))       
        if node.right is not None:
            queue.append((node.right, current_level + 1))
    return height


# if __name__ == "__main__":

#     n = int(input())
#     node_list = [int(x) for x in input().split(" ")]
#     Tree = BinarySearchTree()
#     for i in range(n):
#         Tree.create(node_list[i])

#     print(Tree.get_height())