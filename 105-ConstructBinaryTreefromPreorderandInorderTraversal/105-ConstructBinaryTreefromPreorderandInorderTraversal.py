# Last updated: 24/06/2025, 12:43:51
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.preorder_idx = 0
        self.inorder_idx_map = {}

        for i, val in enumerate(inorder):
            self.inorder_idx_map[val] = i

        return self.build_subtree(0, len(inorder)-1, preorder,inorder)

    def build_subtree(self, left, right, preorder, inorder):
        if left > right:
            return None

        val = preorder[self.preorder_idx]

        inorder_idx = self.inorder_idx_map[val]
        node = TreeNode(val)

        self.preorder_idx += 1

        node.left = self.build_subtree(left, inorder_idx -1, preorder, inorder)
        node.right = self.build_subtree(inorder_idx +1, right, preorder, inorder)

        return node