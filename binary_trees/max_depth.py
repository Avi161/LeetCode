# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ## Recursive DFS 
        
        # return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))

        ## Iterative DFS

        stack = [[root,1]]
        res = 0

        while stack:
            node, depth = stack.pop()
            
            res = max(res, depth)
            if node.left:
                stack.append([node.left, depth+1])
            if node.right:
                stack.append([node.right, depth+1])
        
        return res

        ## BFS

        # q = deque([root])
        # level = 0
        # while q:
        #     length = len(q)
            
        #     for i in range(length):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level