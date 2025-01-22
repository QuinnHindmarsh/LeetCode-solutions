from collections import deque
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        #not enough cables
        if len(connections) < n-1:
            return -1
        
        visited = [False]*n
        components = 0
        adjList = {i:[] for i in range(n)}

        for edge in connections: 
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        def BFS(start):
            visited[start] = True
            q = deque()
            q.append(start)

            while q:
                node = q.popleft()
                for neighbour in adjList[node]:
                    if visited[neighbour] == False:
                        visited[neighbour] = True
                        q.append(neighbour)


        for i in range(len(visited)):
            if visited[i] == False:
                BFS(i)
                components +=1

        return components -1

            


                

        

