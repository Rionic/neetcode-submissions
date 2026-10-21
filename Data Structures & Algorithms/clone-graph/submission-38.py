"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

        val = int
        neighbors = [Node, Node, ...]
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        oldToNew = {}

        def dfs(node):

            if node in oldToNew:
                return

            newNode = Node(node.val)
            oldToNew[node] = newNode

            for nei in node.neighbors:
                dfs(nei)
                newNode.neighbors.append(oldToNew[nei])
            
        dfs(node)
        return oldToNew[node]
        