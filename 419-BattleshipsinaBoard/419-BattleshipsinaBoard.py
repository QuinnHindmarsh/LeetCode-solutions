# Last updated: 01/03/2026, 12:03:46
1class Solution:
2    def countBattleships(self, board: List[List[str]]) -> int:
3        count = 0
4
5        for i in range(len(board)):
6            for j in range(len(board[0])):
7                if board[i][j] == '.':
8                    continue
9                
10                if i > 0 and board[i-1][j] == 'X':
11                    continue
12                
13                if j > 0 and board[i][j-1] == 'X':
14                    continue
15                
16                count += 1
17        
18        return count