class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        vals = []
        # Easy recursive Inorder Traversal to get our values to insert.
        def inord(node):
            if not node:
                return
            inord(node.left)
            vals.append(node.val)
            inord(node.right)
            
        inord(root)
        # Create a new tree to return.
        tree = TreeNode(val=vals[0])
		# Use a sentinel so we dont lose our tree location in memory.
        tmp = tree
		# Iterate through our vals, creating a new right node with the current val.
        for i in vals[1:]:
            tmp.right = TreeNode(val=i)
			# Move the sentinel to the next node.
            tmp = tmp.right
            
        return tree