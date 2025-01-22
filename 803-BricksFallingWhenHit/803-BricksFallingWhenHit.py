class Solution:
    def hitBricks(self, grid, hits):
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                size[root_b] += size[root_a]
                parent[root_a] = root_b


        rows, cols = len(grid), len(grid[0])
      
        parent = list(range(rows * cols + 1))
        size = [1] * (rows * cols + 1)


        grid_copy = deepcopy(grid)
        for i, j in hits:
            grid_copy[i][j] = 0

        for j in range(cols):
            if grid_copy[0][j] == 1:
                union(j, rows * cols)


        for i in range(1, rows):
            for j in range(cols):
                if grid_copy[i][j] == 0:
                    continue
                if grid_copy[i - 1][j] == 1:
                    union(i * cols + j, (i - 1) * cols + j)
                if j > 0 and grid_copy[i][j - 1] == 1:
                    union(i * cols + j, i * cols + j - 1)

        ans = []
      
        for i, j in reversed(hits):
            if grid[i][j] == 0:
                ans.append(0)
                continue
            grid_copy[i][j] = 1
            prev_size = size[find(rows * cols)]
          
            if i == 0:
                union(j, rows * cols)
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x, y = i + delta_row, j + delta_col
                if 0 <= x < rows and 0 <= y < cols and grid_copy[x][y] == 1:
                    union(i * cols + j, x * cols + y)
            curr_size = size[find(rows * cols)]
          

            ans.append(max(0, curr_size - prev_size - 1))
        return ans[::-1]