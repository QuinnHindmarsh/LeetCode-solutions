class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minArr = [0,0]

        for i in range(2,len(cost)):
            minArr.append(min(minArr[i-1] + cost[i-1], minArr[i-2] + cost[i-2]))

        return min(minArr[-1] + cost[-1], minArr[-2] + cost[-2])