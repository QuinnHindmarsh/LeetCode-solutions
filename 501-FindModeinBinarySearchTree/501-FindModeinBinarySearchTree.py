# Last updated: 02/03/2026, 12:08:50
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def findMode(self, root: Optional[TreeNode]) -> List[int]:
9        freq = defaultdict(int)
10
11        def dfs(node): 
12            if not node: 
13                return 
14            
15            freq[node.val] += 1
16            dfs(node.left)
17            dfs(node.right)
18
19        dfs(root)
20        mx_freq = max(freq.values())
21
22        ans = []
23        for key, value in freq.items(): 
24            if value == mx_freq: 
25                ans.append(key)
26        return ans