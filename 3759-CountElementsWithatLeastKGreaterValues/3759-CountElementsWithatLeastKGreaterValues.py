# Last updated: 02/04/2026, 12:41:36
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        if n < 0:
4            x = 1 / x
5            n = -n
6        
7        result = 1
8        while n > 0:
9            if n % 2 == 1:    
10                result *= x
11            x *= x             
12            n //= 2            
13        return result