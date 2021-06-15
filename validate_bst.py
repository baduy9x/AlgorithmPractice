""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check(root, MIN, MAX):
    if root is None:
        return True
    if root.left is None and root.right is None:
        if MIN < root.data < MAX:
            return True
        return False
    
    return check(root.left, MIN, root.data) and check(root.right, root.data, MAX)

def checkBST(root):
    return check(root, -float("inf"), float("inf"))

