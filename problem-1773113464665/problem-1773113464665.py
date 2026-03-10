# Last updated: 10/03/2026, 14:01:04
1class Solution:
2    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
3        freq = Counter(nums)
4
5        if len(nums) % k != 0:
6            return False
7
8        heap = list(set(nums))
9        heapq.heapify(heap)
10
11        while heap:
12            top = heap[0]
13
14            for i in range(k): 
15                if freq[top +i] == 0: 
16                    return False
17                freq[top +i] -=1
18
19                if freq[top + i] == 0 and top + i != heapq.heappop(heap):
20                    return False
21
22        return True