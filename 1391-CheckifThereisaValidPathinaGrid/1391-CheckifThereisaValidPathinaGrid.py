class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        q.append((0,0))
        seen = set()

        while q:
            i,j = q.popleft()
            v = grid[i][j]


            seen.add((i,j))
            
            if i == n -1 and j == m -1:
                return True

            if v == 1:
                if j > 0 and (i,j-1) not in seen:
                    left = grid[i][j-1]
                    if left == 4 or left == 1 or left == 6:
                            q.append((i,j-1))
                
                if j < m -1 and (i,j+1) not in seen:
                    right = grid[i][j+1]
                    if right == 3 or right == 1 or right == 5:
                        q.append((i,j+1))


            elif v == 2:
                if i > 0 and (i-1,j) not in seen:
                    up = grid[i-1][j]
                    if up == 3 or up == 4 or up == 2:
                        q.append((i-1, j))

                if i < n - 1 and (i+1,j) not in seen:
                    down = grid[i+1][j]
                    if down == 5 or down == 6 or down ==2:
                        q.append((i+1,j))
                
            elif v == 3:

                if i < n - 1 and (i+1,j) not in seen:
                    down = grid[i+1][j]
                    if down == 2 or down == 5 or down == 6:
                        q.append((i+1,j))
                

                if j > 0 and (i,j-1) not in seen:
                    left = grid[i][j-1]
                    if left == 4 or left == 1 or left == 6:
                        q.append((i,j-1))
                
            elif v == 4:
                if i < n - 1 and (i+1,j) not in seen:
                    down = grid[i+1][j]
                    if down == 5 or down == 6 or down == 2:
                        q.append((i+1,j))
                
                if j < m -1 and (i,j+1) not in seen:
                    right = grid[i][j+1]
                    if right == 3 or right == 1 or right == 5:
                        q.append((i,j+1))

            elif v == 5:
                if i > 0 and (i-1,j) not in seen:
                    up = grid[i-1][j]
                    if up == 3 or up == 4 or up ==2:
                        q.append((i-1, j))


                if j > 0 and (i,j-1) not in seen:
                    left = grid[i][j-1]
                    if left == 1 or left == 4 or left == 6:
                        q.append((i,j-1))

            elif v == 6:
                if i > 0 and (i-1,j) not in seen:
                    up = grid[i-1][j]
                    if up == 3 or up == 4 or up == 2:
                        q.append((i-1, j))

                if j < m -1 and (i,j+1) not in seen:
                    right = grid[i][j+1]
                    if right == 1 or right == 5 or right == 3:
                        q.append((i,j+1))



        return False
