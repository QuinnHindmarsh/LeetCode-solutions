# Last updated: 23/06/2025, 18:19:12
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 0))
        stack = []
        mx = 0
        
        while q:
            l = float('inf')
            r = 0

            while q:
                node, idx = q.popleft()
                stack.append((node, idx))

            while stack:
                node, idx = stack.pop()\

                if not node:
                    continue

                l = min(idx, l)
                r = max(idx, r)


                q.append((node.left, idx *2 +1))
                q.append((node.right, idx*2 + 2))

            mx = max(mx, (r -l) +1)
                

        return mx