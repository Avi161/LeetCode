from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
#        1
#     2    3
#   4  5  10


# Initialization of the Binary tree
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

head = A

# BFS 

def bfs(node):
    q = deque()
    q.append(node)
    ans = []

    while q:
        node = q.popleft()
        ans.append(node.val)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

    return ans

print("Level Order Traversal: ", bfs(head))