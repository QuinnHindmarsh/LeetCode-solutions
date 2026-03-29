# Last updated: 29/03/2026, 13:53:58
1class dsu: 
2    def __init__(self,n): 
3        self.parent = [i for i in range(n)]
4        self.rank = [0] * n 
5        self.parity = [0] * n 
6
7    def find(self,x): 
8        if self.parent[x] != x:
9            root  = self.find(self.parent[x])
10            
11            self.parity[x] ^= self.parity[self.parent[x]]
12            self.parent[x] = root 
13        return self.parent[x]
14
15    def union(self,x,y,w):
16        parentX = self.find(x)
17        parentY = self.find(y)
18
19        if parentY == parentX: 
20            return self.parity[y] ^ self.parity[x] ^ w == 0 
21
22
23        if self.rank[parentX] < self.rank[parentY]: 
24            parentX, parentY = parentY, parentX
25            x,y = y,x
26
27        self.parent[parentY] = parentX
28        self.parity[parentY] = self.parity[x] ^ self.parity[y] ^ w
29        if self.rank[parentX] == self.rank[parentY]:
30            self.rank[parentY] +=1
31        return True
32
33class Solution:
34    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
35        unionfind = dsu(n)
36        cnt = 0 
37
38        for u,v,w in edges: 
39            if unionfind.union(u,v,w): 
40                cnt += 1
41
42        return cnt
43
44
45        