# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        count = 0
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            count += 1
            if count == k:
                return node.val

            cur = node.right

        #Recursive
        # arr = []

        # def dfs(node):
        #     if not node:
        #         return
            
        #     dfs(node.left)
        #     arr.append(node.val)
        #     dfs(node.right)
        
        # dfs(root)
        # return arr[k - 1]
