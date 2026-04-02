# Last updated: 02/04/2026, 11:57:33
1class Solution:
2    def countElements(self, nums: List[int], k: int) -> int:
3        greater = 0 
4        last_number = None 
5        count_of_last = 0 
6        ans = 0 
7
8        heap = nums 
9        heapify_max(heap)
10
11        while heap:
12            num = heappop_max(heap) 
13            if num == last_number: 
14                count_of_last += 1
15            else:
16                greater += count_of_last
17                count_of_last = 1
18                last_number = num
19
20            if greater >= k: 
21                ans += 1
22
23        return ans