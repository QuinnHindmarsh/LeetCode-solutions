# Last updated: 06/04/2026, 19:18:57
1class Solution:
2    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
3        optimal = [0] * (max(worker)+1)
4        total =     mx = 0 
5        
6        for p,d in zip(profit,difficulty):
7            if d >= len(optimal):
8                continue 
9            optimal[d] = max(p, optimal[d])
10
11
12        for i in range(len(optimal)): 
13            mx = max(mx, optimal[i])
14
15            optimal[i] =mx
16
17
18        for w in worker: 
19            total += optimal[w]
20
21        return total 