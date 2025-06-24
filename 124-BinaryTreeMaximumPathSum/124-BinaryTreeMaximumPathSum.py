# Last updated: 24/06/2025, 13:51:43
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mx = -float('inf')

        self.mx = max(self.dfs(root), self.mx)

 
        return self.mx

    def dfs(self, node):
        if not node:
            return 0 
        
        left = max(self.dfs(node.left), 0)
        right = max(self.dfs(node.right), 0)

        self.mx = max(self.mx, left + right + node.val)
        return max(left,right) + node.val