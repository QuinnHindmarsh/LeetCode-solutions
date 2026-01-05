# Last updated: 05/01/2026, 15:05:42
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
9        ans = []
10        path = []
11        def dfs(node):
12            if not node:
13                return
14            
15            path.append(str(node.val))
16            dfs(node.left)
17            dfs(node.right)
18            
19            if not node.left and not node.right:
20                ans.append("->".join(path))
21            path.pop()
22
23
24
25        dfs(root)
26        return ans