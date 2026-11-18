# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, lo, hi):
            if not node:
                return True
            if not (lo < node.val < hi):
                return False
            
            # Going left means all must be < node.val
            return (dfs(node.left, lo, min(hi, node.val)) and 
                    dfs(node.right, max(lo, node.val), hi))


        return (dfs(root.left, float('-inf'), root.val) and
                dfs(root.right, root.val, float('inf')))
        