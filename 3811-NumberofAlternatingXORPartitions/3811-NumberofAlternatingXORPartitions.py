# Last updated: 05/04/2026, 09:16:52
1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3        
4        def can_ship(weights,days,capacity): 
5            day_count = used = 0 
6
7            for parcel in weights: 
8                if used + parcel > capacity: 
9                    used = 0 
10                    day_count += 1
11                    if day_count >= days: 
12                        return False
13                used += parcel
14            return True
15
16        l,r = max(weights), sum(weights)
17
18        while l < r: 
19            mid = (l+r)//2
20
21            if can_ship(weights,days,mid): 
22                r = mid
23            else: 
24                l = mid +1
25        return l