# Last updated: 07/12/2025, 09:47:45
1class Solution:
2    def minSteps(self, n: int) -> int:
3        ans = 0
4
5        # Work my way backwards
6
7        # Clip board size - recursive?
8        # 3 - 1 char - 3 moves
9        # 7 - 7 - 1 char
10        # 10 - 5 char - 7 moves
11        # 24 
12
13        # Even, half until it hits 0, each time you half add 2 moves 
14        # odd, 
15
16        # 5 10 15
17        # 5 7  8 
18        
19        # Odd, greatest divsor repeat untill you hit 0
20
21        # Greatist proper devider
22        def GPD(num):
23            for i in range(2,isqrt(num)+1):
24                if num % i == 0:
25                    return num // i
26            return 1
27
28        def steps(num):
29            if num == 1: return 0
30            if num == 2: return 2
31
32            gpd = GPD(num)
33            if gpd == 1:
34                return num 
35            return (num // gpd) + steps(gpd)
36        
37        return steps(n)