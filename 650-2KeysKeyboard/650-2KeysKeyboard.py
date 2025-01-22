class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0

        # Work my way backwards

        # Clip board size - recursive?
        # 3 - 1 char - 3 moves
        # 7 - 7 - 1 char
        # 10 - 5 char - 7 moves
        # 24 

        # Even, half until it hits 0, each time you half add 2 moves 
        # odd, 

        # 5 10 15
        # 5 7  8 
        
        # Odd, greatest divsor repeat untill you hit 0

        # Greatist proper devider
        def GPD(num):
            for i in range(2,isqrt(num)+1):
                if num % i == 0:
                    return num // i
            return 1

        def steps(num):
            if num == 1: return 0
            if num == 2: return 2

            if num % 2 == 0:
                return 2 + steps(num//2)

            gpd = GPD(num)
            print(gpd)
            if gpd == 1:
                return num 
            return (num // gpd) + steps(gpd)
        
        return steps(n)