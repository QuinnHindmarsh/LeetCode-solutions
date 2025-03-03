class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        p1 = 0
        p2 = 0
        n = len(player1)

        for i in range(n):
            if (i >= 2 and player1[i-2] == 10) or (i>= 1 and player1[i-1] == 10):
                p1 += player1[i]
            if (i >= 2 and player2[i-2] == 10) or (i>= 1 and player2[i-1] == 10):
                p2 += player2[i]
            p1 += player1[i]
            p2 += player2[i]
                
        if p2 > p1:return 2
        if p2 < p1: return 1
        return 0