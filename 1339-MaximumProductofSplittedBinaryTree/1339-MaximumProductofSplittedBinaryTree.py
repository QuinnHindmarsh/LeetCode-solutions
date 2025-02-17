# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtreeVals = {}

        def calc_subtree_vals(node):
            if node in subtreeVals:
                return subtreeVals[node]

            lsum = 0
            rsum = 0
            csum = node.val

            if node.left:
                lsum = calc_subtree_vals(node.left)
            if node.right: 
                rsum = calc_subtree_vals(node.right)

            subtreeVals[node] = lsum + rsum + csum
            return subtreeVals[node]


        def max_traversal(node):
            c = subtreeVals[node] * (total - subtreeVals[node])
            l = 0
            r = 0 

            if node.left:
                l = max_traversal(node.left)
            if node.right:
                r = max_traversal(node.right)

            return max(c, l, r) 
        
        calc_subtree_vals(root)
        total = subtreeVals[root] 

        return max_traversal(root) % 1000000007
