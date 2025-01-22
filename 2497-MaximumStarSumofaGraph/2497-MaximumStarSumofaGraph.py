class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        ans = max(vals)
        adjList = [[] for i in range(len(vals))]
        

        for s,e in edges:
            adjList[s].append(vals[e])
            adjList[e].append(vals[s])


        for i  in range (len(adjList)):
            adjList[i].sort(reverse=True)
            kSum = vals[i]

            for j in range(k):
                if j == len(adjList[i]):
                    break
                if adjList[i][j] < 0:
                    break
                kSum += adjList[i][j]
            
            ans = max(ans,kSum)

        return ans