# Last updated: 23/03/2026, 21:17:49
1class Solution:
2    def fib(self, n: int) -> int:
3        
4        if n < 2: 
5            return n
6
7        last1 = 1
8        last2 = 0
9        
10
11        for i in range(2,n+1): 
12            temp = last1 + last2
13            last2 = last1
14            last1 = temp
15
16        return last1