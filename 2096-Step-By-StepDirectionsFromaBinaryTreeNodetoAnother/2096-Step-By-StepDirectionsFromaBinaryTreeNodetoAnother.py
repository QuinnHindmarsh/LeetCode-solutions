# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
       
        
        # Finds the path from given not to target node 
        # Assuming the target node exists in a subtree with the given node as the root
        # A list is used to give O(h) space, instead of O(nh) that would be used with a string (assuming you pass the string as a param)
        def traversal(node, tar):
            if node.val == tar:
                return path 
            
            if node.left:
                path.append('L')
                left_result = traversal(node.left, tar)
                if left_result:
                    return left_result
                path.pop()

            if node.right:
                path.append('R')
                right_result = traversal(node.right, tar)
                if right_result:
                    return right_result
                path.pop()
            return None



        # Path from root to start 
        # And path from root to end
        path = []
        sp = traversal(root,startValue)
        path = []
        ep = traversal(root,destValue)
        ansPath = ''
        node = root

        i = 0
        # Finds the LCA (lowest commen ancestor) and sets the root to it
        while i < len(sp) and i < len(ep) and sp[i] == ep[i]:
            if ep[i] == 'L':
                node = node.left
                i +=1
            else:
                node = node.right
                i +=1
        
        # The point node will now be at will be the first node where either the start node 
        # Is at a different side as the end node 
        # Or we are either at the start or end node


        # If this Triggers we have arrived at the destination node, but not yet the start
        # This means we can just up up as many times as itterations we need to do 
        if i < len(sp) and i >= len(ep):
            while i < len(sp) and i >= len(ep):
                ansPath += 'U'
                i +=1
            return ansPath


        # We have arrived at the start point but not the end
        # the end point is a child of the start point
        if i < len(ep) and i >= len(sp):
            path = []
            return ''.join(traversal(node,destValue))

        # Otherwise we are at a point where the start and dest are at different sides of the current node
        # go up until the start path is at the LCA, then take the path from the LCA to end noed

        j = i 
        while j < len(sp):
            ansPath += 'U'
            j +=1

        while i < len(ep):
            ansPath += ep[i]
            i +=1

        return ansPath


