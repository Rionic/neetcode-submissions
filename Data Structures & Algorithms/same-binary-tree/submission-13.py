# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def build_list(root, arr):
            if not root:
                arr.append(None)
                return
            arr.append(root.val)

            build_list(root.left, arr)
            build_list(root.right, arr)

            return arr
        p_arr, q_arr = [], []
        return build_list(p, p_arr) == build_list(q, q_arr)

