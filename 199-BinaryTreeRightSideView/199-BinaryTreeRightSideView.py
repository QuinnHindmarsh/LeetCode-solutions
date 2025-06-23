# Last updated: 23/06/2025, 17:39:13
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        ans = []
        q.append((root, 0))

        while q:
            node, layer = q.popleft()

            if not node:
                continue

            if len(ans) == layer:
                ans.append(node.val)
            
            q.append((node.right, layer +1))
            q.append((node.left, layer+1))
        
        return ans