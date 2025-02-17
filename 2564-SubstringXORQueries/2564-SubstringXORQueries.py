class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        intMap = {}
        n = len(s)
        ans = []

        for i in range(n):
            cur = 0 
            if s[i] == '0':
                if 0 not in intMap:
                    intMap[0] = (i,i)
                continue

            for j in range(i,min(n, i + 32)):
                cur *= 2
                cur += int(s[j])

                if cur not in intMap:
                    intMap[cur] = (i,j)

        for q in queries:
            val = q[0] ^ q[1]

            if val in intMap:
                ans.append(list(intMap[val]))
            else:
                ans.append([-1,-1])

        return ans