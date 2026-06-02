# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.height = 0
        # if not root: return 0
        def calc(root, h):

            if not root:
                self.height = max(self.height, h)
                return
            
            calc(root.left, h + 1)
            calc(root.right, h + 1)

        calc(root, 0)

        return self.height
        