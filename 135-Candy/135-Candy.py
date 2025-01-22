class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        l2r = []
        r2l = [0] * n
        candy = [1] * n
        

        for i in range(n-1):
            if ratings[i] > ratings[i+1]:
                l2r.append(1)
            else:
                l2r.append(0)
        l2r.append(0)

        for i in range(n-2, -1, -1):
            if l2r[i] == 1:
                l2r[i] += l2r[i+1]

        

        for i in range(n-1,0,-1):
            if ratings[i] > ratings[i-1]:
                r2l[i] = 1
        
        for i in range(1,n):
            if r2l[i] == 1:
                r2l[i] += r2l[i-1]
        
        
        for i in range(n):
            candy[i] += max(l2r[i], r2l[i])

        return sum(candy)

        