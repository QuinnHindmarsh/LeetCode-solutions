# Last updated: 25/06/2025, 12:27:49
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.visited = {}

        if not node:
            return None
        
        return self.dfs(node)

        


    def dfs(self, node):
        new_node = Node(node.val)
        self.visited[node] = new_node

        if not node.neighbors:
            return Node(node.val)

        else:

            for child in node.neighbors:
                if child not in self.visited:

                    new_node.neighbors.append(self.dfs(child))
                else:
                    new_node.neighbors.append(self.visited[child])

        return new_node


