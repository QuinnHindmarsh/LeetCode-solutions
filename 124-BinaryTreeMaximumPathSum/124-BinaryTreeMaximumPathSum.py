# Last updated: 24/06/2025, 13:49:39
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mx = -float('inf')
        self.is_positive_node = False
        self.max_node = -float('inf')

        self.mx = max(self.dfs(root), self.mx)

        if not self.is_positive_node:
            return self.max_node
        return self.mx

    def dfs(self, node):
        if not node:
            return 0 
        
        if node.val > 0:
            self.is_positive_node = True

        self.max_node = max(self.max_node, node.val) 

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.mx = max(self.mx, left + right + node.val, node.val)
        return max(max(left,right,0) + node.val, 0)