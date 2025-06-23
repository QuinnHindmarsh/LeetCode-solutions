# Last updated: 23/06/2025, 19:31:29
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, target, arr):
            if node == target:
                return arr

            if not node:
                return 
            
            arr.append('l')
            if dfs(node.left,target,arr):
                return arr
            arr.pop()

            arr.append('r')
            if dfs(node.right, target, arr):
                return arr
            arr.pop()

            return 

        p_path = dfs(root, p, [])
        q_path = dfs(root, q, [])

        node = root

        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] != q_path[i]:
                break
            
            if p_path[i] == 'r':
                node = node.right
            else:
                node = node.left
        return node