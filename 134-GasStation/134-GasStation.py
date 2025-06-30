# Last updated: 30/06/2025, 16:13:14
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        tank = start = 0 

        for i in range(len(gas)):

            tank += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                start = i + 1

        return start