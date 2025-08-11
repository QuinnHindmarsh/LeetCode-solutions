# Last updated: 11/08/2025, 14:06:02
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        self.dp = {}
        self.end = (len(grid)-1, len(grid[0])-1)
        self.grid = grid
        self.cords = [[1,0],[-1,0], [0,-1], [0,1]]

        self.dfs(0,0,health)



        if self.end in self.dp:
            return True
        return False

    def dfs(self,i,j,hp):
        if i >= len(self.grid) or i < 0 or j >= len(self.grid[0]) or j < 0:
            return

        if self.grid[i][j] == 1:
            hp -=1

        if hp <= 0:
            return 
        
        if (i,j) == self.end:
            self.dp[(i,j)] = hp


        if (i,j) in self.dp and self.dp[(i,j)] >= hp:
            return
        else:
            self.dp[(i,j)] = hp


        for x,y in self.cords:
            self.dfs(i + x, j + y, hp)

        