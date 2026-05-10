# Last updated: 10/05/2026, 13:11:39
1class Solution:
2    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
3
4        adj_way_there = {}
5        adj_way_back = {}
6
7        for i in range(n):
8            adj_way_there[i] = []
9            adj_way_back[i] = []
10
11        for s,e,c,m in roads: 
12            adj_way_there[s].append((c,e))
13            adj_way_there[e].append((c,s))
14
15            adj_way_back[s].append((c*m,e))
16            adj_way_back[e].append((c*m,s))
17
18
19        def dj(graph,start):
20            ans = {}
21
22            for node in graph.keys(): 
23                ans[node] = float('inf')
24
25            ans[start] = 0
26
27            pq = [(0,start)]
28
29            while pq:
30
31                cur_dist, cur_node = heapq.heappop(pq)
32
33                if cur_dist > ans[cur_node]: 
34                    continue 
35
36
37                for weight, neithbour in graph[cur_node]:
38                    distance = cur_dist + weight
39    
40                    if distance < ans[neithbour]: 
41                        ans[neithbour] = distance
42                        heapq.heappush(pq,(distance,neithbour))
43
44
45            return ans
46
47        ans = []
48
49        
50        for start in range(n): 
51            cost_there = dj(adj_way_there,start)
52            cost_back = dj(adj_way_back,start)
53            mn = float('inf')
54            
55            for i in range(n): 
56                mn = min(cost_there[i] + cost_back[i] + prices[i],mn)
57
58            ans.append(mn)
59
60        return ans