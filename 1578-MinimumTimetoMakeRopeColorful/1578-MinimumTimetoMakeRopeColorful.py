# Last updated: 03/11/2025, 13:15:38
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0 

        for i in range(1,len(colors)):
            if colors[i] == colors[i-1]:
                ans += min(neededTime[i],neededTime[i-1])
                
                neededTime[i] = max(neededTime[i],neededTime[i-1])


        return ans