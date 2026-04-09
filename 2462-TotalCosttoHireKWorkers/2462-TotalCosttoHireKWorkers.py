# Last updated: 10/04/2026, 08:45:57
1class Solution:
2    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
3        heap = []
4        n = len(costs)
5        l,r = 0, n-1
6        ans = 0 
7
8        if candidates * 2 >= len(costs):
9            for idx, c in enumerate(costs):
10                heappush(heap,(c,idx))
11
12            r = -1
13            l = n 
14        else: 
15            
16            while l < candidates: 
17                heappush(heap,(costs[l],l))
18                l += 1
19 
20            while r > n-1 - candidates: 
21                heappush(heap,(costs[r],r))
22                r -=1
23
24        for _ in range(k): 
25            c, idx = heappop(heap) 
26            ans += c
27
28            if not l <= r:
29                continue
30
31            if idx > r and r >= 0: 
32                heappush(heap,(costs[r],r))
33                r -=1
34
35            elif idx < l and l < n: 
36                heappush(heap,(costs[l],l))
37                l+=1
38
39
40        return ans