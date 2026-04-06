# Last updated: 06/04/2026, 10:36:31
1class Solution:
2    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
3        users_minutes = defaultdict(int)
4
5        logs.sort()
6
7        for i in range(len(logs)): 
8            if i > 0 and logs[i] == logs[i-1]: 
9                continue 
10            user_id, _minute = logs[i]
11
12            users_minutes[user_id]+=1
13
14        ans = [0] * k
15
16        for minutes in users_minutes.values(): 
17            ans[minutes-1] +=1
18
19        return ans
20