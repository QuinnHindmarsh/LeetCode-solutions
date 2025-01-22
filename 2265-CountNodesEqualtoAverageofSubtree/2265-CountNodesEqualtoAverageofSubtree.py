# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def avg_nodes(node):
            avg = node.val
            nc = 1

            if node.left:
                data = avg_nodes(node.left)
                avg += data[0]
                nc += data[1]

            if node.right:
                data = avg_nodes(node.right)
                avg += data[0]
                nc += data[1]

            if node.val == avg // nc:
                self.count +=1
            
            return [avg,nc]
        
        avg_nodes(root)
        return self.count