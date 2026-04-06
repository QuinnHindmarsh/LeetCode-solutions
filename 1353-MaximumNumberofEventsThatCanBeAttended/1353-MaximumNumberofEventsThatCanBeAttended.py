# Last updated: 06/04/2026, 12:39:17
1class Solution:
2    def maxEvents(self, events: List[List[int]]) -> int:
3        events.sort()
4        heap = []
5        i, n, attended = 0, len(events), 0
6        day = 1
7
8        while i < n or heap:
9            if not heap:
10                day = events[i][0]
11                
12            while i < n and events[i][0] <= day:
13                heapq.heappush(heap, events[i][1])
14                i += 1
15            while heap and heap[0] < day:
16                heapq.heappop(heap)
17            if heap:
18                heapq.heappop(heap)  
19                attended += 1
20            day += 1
21
22        return attended