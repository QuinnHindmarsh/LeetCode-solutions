# Last updated: 24/02/2026, 19:17:25
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        zipped = list(zip(position, speed))
4        zipped.sort()
5
6        max_time = 0 
7        fleets = 0 
8
9        while zipped: 
10            position, speed = zipped.pop()
11
12            time_to_destination = (target - position) / speed
13            if time_to_destination > max_time: 
14                max_time = time_to_destination
15                fleets += 1
16
17        return fleets