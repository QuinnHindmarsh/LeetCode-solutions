class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def seive(num):
            # 1 indexed
            primes = [True] *(num+1)

            primes[0] = False
            primes[1] = False

            for i in range(2,num+1):
                if primes[i]:
                    for j in range(i*i,num+1,i):
                        primes[j] = False            
            
            return primes

        primes = seive(right)

        prev = None
        minGap = 999999999
        ans = [-1,-1]

        for i in range(left,right+1):
            if primes[i]:
                if not prev:
                    prev = i
                else:
                    if i - prev < minGap:
                        minGap = i - prev
                        ans = [prev,i]
                    prev = i
        return ans
                