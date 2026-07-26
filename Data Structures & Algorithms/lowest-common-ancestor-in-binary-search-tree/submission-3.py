# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.trav_q = []
        self.trav_p = []

        def find(node, val1, isP):
            if isP:
                self.trav_p.append(node)
            else:
                self.trav_q.append(node)
            if node.val == val1:
                return
            if node.val > val1:
                find(node.left, val1, isP)
            elif node.val < val1:
                find(node.right, val1, isP)

        find(root, p.val, True)
        find(root, q.val, False)
        
        i = 0
        while i < len(self.trav_q) and i < len(self.trav_p) and self.trav_q[i] == self.trav_p[i]:
            i += 1
        return self.trav_q[i - 1]

        