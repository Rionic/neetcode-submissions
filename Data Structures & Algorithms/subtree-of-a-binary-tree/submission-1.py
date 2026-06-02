# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        self.same = False
        
        def build_list(root, arr):
            if not root:
                arr.append(None)
                return
            else:
                arr.append(root.val)

            build_list(root.left, arr)
            build_list(root.right, arr)

            return arr

        def dfs(root, subRoot):
            if not self.same and root:
                if root.val == subRoot.val:
                    p, q = [], []
                    self.same = build_list(root, p) == build_list(subRoot, q)
                dfs(root.left, subRoot)
                dfs(root.right, subRoot)
            
            return self.same

        return dfs(root, subRoot)
        