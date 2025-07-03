# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # def check(node):
        #     if not node:
        #         return 0  # height of null node is 0
            
        #     left = check(node.left)
        #     if left == -1:
        #         return -1  # unbalanced
            
        #     right = check(node.right)
        #     if right == -1:
        #         return -1  # unbalanced
            
        #     if abs(left - right) > 1:
        #         return -1  # current node is unbalanced
            
        #     return 1 + max(left, right)  # return height
        
        # return check(root) != -1

        def dfs(root):
            if not root:
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1

            return [balanced, 1+max(left[1], right[1])]