# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    balance = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):

            if not root:
                return 0

            l = 1 + dfs(root.left)
            r = 1 + dfs(root.right)

            if abs(r - l) > 1:
                self.balance = False
            print('r', r, 'l', l)
            return max(l, r)
            
        dfs(root)
        return self.balance

