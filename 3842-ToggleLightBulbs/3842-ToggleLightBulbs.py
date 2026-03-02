# Last updated: 03/03/2026, 10:05:07
1class Solution:
2    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
3        lights = [0] * 100
4        lights_on = []
5
6        for idx in bulbs:
7            idx -=1 
8            lights[idx] ^= 1
9        
10        for idx in range(len(lights)):
11            if lights[idx]:
12                lights_on.append(idx+1)
13        return lights_on