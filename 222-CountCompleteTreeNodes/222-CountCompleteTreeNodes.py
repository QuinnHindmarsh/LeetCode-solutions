# Last updated: 05/01/2026, 14:59:46
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def countNodes(self, root: Optional[TreeNode]) -> int:
9        def dfs(node):
10            if not node:
11                return 0
12            return 1 + dfs(node.left) + dfs(node.right)
13
14        return dfs(root)