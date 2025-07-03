# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.isSame = False
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            dfs(root.right)
            check = self.sameTree(root, subRoot)

            if check == True:
                self.isSame = True
                return 
        dfs(root)
        return self.isSame
    
    
    def sameTree(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        
        if tree1 and tree2 and tree1.val == tree2.val:
            return self.sameTree(tree1.left, tree2.left) and self.sameTree(tree1.right, tree2.right)
        else:
            return False