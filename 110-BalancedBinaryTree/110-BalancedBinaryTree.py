# Last updated: 23/06/2025, 17:11:46
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left) 

            right = dfs(node.right) 

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) +1


        return dfs(root) != -1
            