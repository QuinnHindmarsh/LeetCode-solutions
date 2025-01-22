class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank.append(startGene)
        adj = {}



        def find_diff(str1,str2):
            dif = 0

            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    dif +=1 
                    if dif > 1:
                        return False

            if dif == 1:
                return True

        for i in range(len(bank)):
            adj[bank[i]] = []
            for j in range(len(bank)):
                if find_diff(bank[j],bank[i]):
                    adj[bank[i]].append(bank[j])


        q = deque()
        visited = set()

        visited.add(startGene)
        q.append((startGene,0))
        
        node = None
        while q:
            node, cost = q.popleft()
            if node == endGene:
                return cost

            for n in adj[node]:
                if n not in visited:
                    visited.add(n)
                    q.append((n,cost+1))
        return -1
        
