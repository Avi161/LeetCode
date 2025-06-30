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

# Recursive Pre Order Traversal-DFS
my_list = []
def pre_order(node, my_list):
    if not node:
        return 
    
    my_list.append(node.val)
    if node.left:
        pre_order(node.left, my_list)
    if node.right:
        pre_order(node.right, my_list)
    return my_list

print("Pre Order DFS: ",pre_order(head, my_list))

# Recursive In Order Traversal-DFS
my_list = []
def in_order(node, my_list):
    if not node:
        return 
    
    if node.left:
        in_order(node.left, my_list)
    my_list.append(node.val)
    if node.right:
        in_order(node.right, my_list)
    return my_list

print("In Order DFS: ",in_order(head, my_list))

# Recursive Post Order Traversal-DFS
my_list = []
def post_order(node, my_list):
    if not node:
        return 
    
    if node.left:
        post_order(node.left, my_list)
    if node.right:
        post_order(node.right, my_list)
    my_list.append(node.val)
    return my_list

print("Post Order DFS: ",post_order(head, my_list))

# Iterative Pre Order Traversal-DFS
def pre_order_iter(node):
    stack = [node]
    ans = []

    while stack:
        node = stack.pop()
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
        ans.append(node.val)
    return ans

print("Pre Order Iterative DFS: ", pre_order_iter(head))

# Iterative Post Order Traversal-DFS
def post_order_iter(node):
    stack =  [node]
    ans = []
    
    while stack:
        node = stack.pop()
        ans.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

        return ans[::-1]

# Iterative In Order Traversal-DFS
def in_order_iter(node):
    stack = [node]
    cur = node
    ans = []

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        
        cur = stack.pop()
        ans.append(cur.val)
        node = node.right
    return ans

