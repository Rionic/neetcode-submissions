# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lq = []
        lp = []

        def find(node, val1, isP):
            if isP:
                lp.append(node)
            else:
                lq.append(node)
            if node.val == val1:
                return
            if node.val > val1:
                find(node.left, val1, isP)
            elif node.val < val1:
                find(node.right, val1, isP)

        find(root, p.val, True)
        find(root, q.val, False)
        
        i = 0
        while i < len(lq) and i < len(lp) and lq[i] == lp[i]:
            i += 1
        return lq[i - 1]

        