# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        pv, qv = p.val, q.val
        while cur:
            if (cur.val >= pv and cur.val <= qv) or (cur.val >= qv and cur.val <= pv):
                return cur
            elif cur.val > pv and cur.val > qv:
                cur = cur.left
            else:
                cur = cur.right