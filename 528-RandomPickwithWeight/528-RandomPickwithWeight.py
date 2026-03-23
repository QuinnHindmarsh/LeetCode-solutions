# Last updated: 23/03/2026, 21:12:03
1class Solution:
2
3    def __init__(self, w: List[int]):
4        self.prefix_sum = [w[0]]
5        self.sum = sum(w)
6        for i in range(1,len(w)): 
7            self.prefix_sum.append(self.prefix_sum[-1] + w[i])
8
9
10
11    def pickIndex(self) -> int:
12        num = random.randint(1,self.sum) 
13
14        ans = bisect_left(self.prefix_sum,num)
15
16        if ans == len(self.prefix_sum): 
17            return ans - 1
18
19        return ans  
20
21
22# Your Solution object will be instantiated and called as such:
23# obj = Solution(w)
24# param_1 = obj.pickIndex()