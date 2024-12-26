"""
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Solution one - recursive DFS O(n) time, O(h) space on the recursive stack


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        # DFS traversal
        def find_max_depth(node, level):
            if not node.left and not node.right:
                return max(level, self.max)

            if node.right:
                self.max = find_max_depth(node.right, level+1)
            if node.left:
                self.max = find_max_depth(node.left, level+1)

            return self.max

        if root:
            return find_max_depth(root, 1)
        # If root is null hieght is zero
        return 0


# Solution two - BFS O(n) time and O(w) space where w is the width of the tree at the widest point
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If root is null max depth is 0
        if not root:
            return 0

        q = deque()
        q.append(root)

        level = 0

        # BFS
        while q:
            level += 1
            # Remove the whole level each itteration, so we can count the depth not number of nodes
            for i in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return level

# My solution
# https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/6187279/recursive-dfs-iterative-bfs-with-spaceti-a8ht/
