# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def traverse(node, curMax):
            if not node:
                return 0
            if node.val >= curMax:
                self.good += 1
                curMax = node.val

            traverse(node.left, curMax)
            traverse(node.right, curMax)
        traverse(root, float('-inf'))
        return self.good