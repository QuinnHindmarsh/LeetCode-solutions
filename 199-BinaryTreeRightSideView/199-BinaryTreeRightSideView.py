# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def traverse(node, level):
            if level == len(ans):
                ans.append(node.val)
            
            if node.right:
                traverse(node.right, level +1)
            
            if node.left:
                traverse(node.left, level +1)
        
        if root:
            traverse(root,0)
        return ans 