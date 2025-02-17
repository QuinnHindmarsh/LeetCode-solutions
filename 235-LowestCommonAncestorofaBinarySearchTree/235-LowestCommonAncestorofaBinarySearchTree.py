# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_node(node, target, path):
            if node == target:
                return path

            if not node.right and not node.left:
                return -1 

            if node.right:
                path.append('r')
                r = find_node(node.right, target, path)
                if r != -1:
                    return r
                path.pop()

            if node.left:
                path.append('l')
                l = find_node(node.left, target, path)
                if l != -1:
                    return l
                path.pop()

            return -1

            

        p_path = find_node(root, p, [])
        q_path = find_node(root, q, [])

        node = root
        i = 0

        while i < len(q_path) and i < len(p_path) and q_path[i] == p_path[i]:
            if q_path[i] == 'r':
                node = node.right
            else:
                node = node.left
            
            i += 1


        return node