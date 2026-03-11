# Last updated: 11/03/2026, 14:42:11
1class Solution:
2    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
3        last_done = {}
4        days = 0 
5
6        for i in range(len(tasks)):
7            typ = tasks[i]
8            if typ not in last_done or days - last_done[typ] >= space: 
9                days += 1
10                last_done[typ] = days
11                continue
12            next_day = last_done[typ] + space +1
13            days += next_day - days
14            last_done[typ] = days
15        return days