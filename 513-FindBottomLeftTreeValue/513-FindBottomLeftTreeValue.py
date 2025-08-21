# Last updated: 21/08/2025, 15:10:51
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]):
        ans = [-1,-1]

        def dfs(node,level):
            if not node: 
                return

            if level > ans[0]:
                ans[0] = level
                ans[1] = node.val

            dfs(node.left,level+1)
            dfs(node.right, level+1)
            
        dfs(root,0)
        return ans[1]


