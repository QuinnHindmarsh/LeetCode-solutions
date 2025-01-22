class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
  
        if n == 1:
            return 3

        temp = {(0,0):1, (0,1):1, (0,2):0, (1,0):1, (1,1):0, (1,2):0}

        for i in range(n-1):
            res = defaultdict(int)

            res[(0,0)] = (((temp[(0,0)] + temp[(0,1)]) % MOD + temp[(0,2)])) % MOD
            res[1,0] = (((temp[(1,0)] + temp[(1,1)]) % MOD + temp[(1,2)])) % MOD

            res[(0,1)] = temp[(0,0)]
            res[(1,1)] = temp[(1,0)]
            res[(0,2)] = temp[(0,1)]
            res[(1,2)] = temp[(1,1)]

            res[(1,0)] = ((res[(1,0)] + temp[(0,0)]) % MOD + (temp[(0,1)] + temp[(0,2)]) % MOD)

            temp = res



        return sum(temp.values()) % MOD