class Solution:
    def reachableNodes(self, edges: List[List[int]], k: int, n: int) -> int:
        adj = [[] for i in range(n)]
        dist = [k + 1] * n
        
        # Make adj list, with weight being num of child nodes +1
        for e in edges:
            adj[e[0]].append((e[1],e[2]))
            adj[e[1]].append((e[0],e[2]))

        # Run dijkstras
        def dijkstras(start=0):
            dist[start] = 0
            heap = [(dist[start],start)] 

            while heap:
                d, u = heapq.heappop(heap)
                if d > k:
                    break
                for v,w in adj[u]:
                    newDist = d + w +1
                    if newDist < dist[v]:
                        dist[v] = newDist
                        heapq.heappush(heap,(newDist,v))

            # Number of reachible nodes
            return sum(d <= k for d in dist)

        reachible_nodes = dijkstras()
        reachible_subNodes = 0
        # For each edge the amount  of nodes i can visit is min(min(edges[i][0], edges[i][1]) - maxMoves, edges[i][2])
        
        for u, v, cnt in edges:
            a = 0 if dist[u] > k else min(k - dist[u], cnt)
            b = 0 if dist[v] > k else min(k - dist[v], cnt)
            reachible_subNodes += min(a + b, cnt)


        # Add number of origonal nodes i can get to, e.g. all with a cost <= k
        return reachible_subNodes + reachible_nodes