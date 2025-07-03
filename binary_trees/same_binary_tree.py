# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
            
        # if not p or not q:
        #     if not p and not q:
        #         return True
        #     else:
        #         return False
        
        # stack_p = [p]
        # stack_q = [q]

        # while stack_p:
        #     node_p = stack_p.pop()
        #     node_q = stack_q.pop()

        #     if node_p.val != node_q.val:
        #         return False
            
        #     if node_p.left or node_q.left:
        #         if node_p.left and node_q.left:
        #             stack_p.append(node_p.left)
        #             stack_q.append(node_q.left)
        #         else:
        #             return False
            
        #     if node_p.right or node_q.right:
        #         if node_p.right and node_q.right:
        #             stack_p.append(node_p.right)
        #             stack_q.append(node_q.right)
        #         else:
        #             return False
        
        # return True