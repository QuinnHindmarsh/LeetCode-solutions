# Last updated: 01/03/2026, 12:00:47
1class Solution:
2    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
3        heapq.heapify_max(happiness)
4        happyness_sum = 0
5
6        for i in range(k):
7            child_happyness = heapq.heappop_max(happiness)
8            happyness_sum += max(child_happyness - i, 0)
9        
10        return happyness_sum
11
12
13
14
15