# Last updated: 23/06/2025, 19:23:22
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, upper, lower):
            
            if not node:
                return True

            if not(lower < node.val < upper): 
                return False 

            left = dfs(node.left, min(upper, node.val), lower)
            right = dfs(node.right, upper, max(lower, node.val))

            return left != False and right != False

        return dfs(root, float('inf'), -float('inf'))