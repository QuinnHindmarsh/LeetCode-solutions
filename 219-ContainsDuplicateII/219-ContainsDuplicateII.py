# Last updated: 23/03/2026, 20:49:47
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        last = {}
4
5
6        for i,num in enumerate(nums): 
7            if num in last: 
8                if abs(last[num] - i )<= k: 
9                    return True
10
11            last[num] = i 
12
13
14        return False