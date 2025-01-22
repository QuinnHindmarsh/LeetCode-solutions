class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.locs = {}
        self.n = len(grid)
        self.grid = grid

        for i in range(self.n):
            for j in range(self.n):
                self.locs[grid[i][j]] = [i,j]
        

    def adjacentSum(self, value: int) -> int:
        loc = self.locs[value]
        adjSum = 0

        if loc[0] - 1 >= 0:
            adjSum += self.grid[loc[0]-1][loc[1]]
        if loc[0] + 1 < self.n:
            adjSum += self.grid[loc[0]+1][loc[1]]
        if loc[1] - 1 >= 0:
            adjSum += self.grid[loc[0]][loc[1]-1]
        if loc[1] + 1 < self.n:
            adjSum += self.grid[loc[0]][loc[1]+1]

        return adjSum
            

    def diagonalSum(self, value: int) -> int:
        """
        [1,2,3]
        [4,5,6]
        [7,8,9]
        -1,-1
        +1,+1
        -1,+1
        +1,-1
        """
        loc = self.locs[value]
        digSum = 0

        i = loc[0]
        j = loc[1]

        if i -1 >= 0 and j -1 >=0:
            digSum += self.grid[i-1][j-1]
        if i +1 < self.n and j +1 < self.n:
            digSum += self.grid[i+1][j+1]
        if i -1 >= 0 and j +1 < self.n:
            digSum += self.grid[i-1][j+1]
        if i +1 < self.n and j -1 >= 0:
            digSum += self.grid[i+1][j-1]
        
        return digSum



# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)