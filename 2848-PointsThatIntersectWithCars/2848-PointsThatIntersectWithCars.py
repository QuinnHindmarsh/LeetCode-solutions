# Last updated: 25/02/2026, 14:17:40
1class Solution:
2    def numberOfPoints(self, nums: List[List[int]]) -> int:
3        mx = 0 
4        for start,end in nums: 
5            mx = max(mx, start)
6            mx = max(mx, end)
7
8        cars = [0] * (mx+1)
9
10        for start,end in nums:
11            for i in range(start,end+1): 
12                cars[i] = 1
13        
14        return sum(cars)