# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        trav = []
        q = deque([root])

        while q:
            nodes = []
            while q:
                node = q.popleft()
                if node:
                    nodes.append(node)
            trav.append([])
            for nei in nodes:
                trav[-1].append(nei.val)
                if nei.left:
                    q.append(nei.left)
                if nei.right:
                    q.append(nei.right)

        return trav

    # 