class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:


        @lru_cache
        def dp(x,moves,movesLeft):
            if x == y or movesLeft <= 0:
                return moves

            if x <= y:
                return moves + (y - x) 


        
            div1 = div2 = div3 = div4 = moves + (abs(x-y))
            
            rem = x % 11
            rem2 = 11-(x % 11) 

            div1 = min(dp(x//11, moves + (rem+1), movesLeft - (rem+1)), div1)
            div2 = min(dp((x//11) +1, moves + (rem2+1), movesLeft - (rem2+1)), div2)

            rem = x % 5
            rem2 = 5-(x % 5) 
            
            div3 = min(dp(x//5, moves + (rem+1) ,movesLeft - (rem+1)) ,div3)
            div4 =  min(dp((x//5) +1, moves + (rem2+1) ,movesLeft - (rem2+1)) ,div4)


            return min(div1,div2,div3,div4)

            
               
        return dp(x,0,abs(y-x))


#
