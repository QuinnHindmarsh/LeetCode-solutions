class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n

        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1

        degree.sort()

        maxVal = 0

        for i in range(len(degree)):
            maxVal += (degree[i] * (i+1))
        return maxVal