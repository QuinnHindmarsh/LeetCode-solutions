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
