class Solution:
    def smallestValue(self, n: int) -> int:
        seen = set()
        mn = 1e6
        
        def sieve(n):
            isPrime = [True] * (n + 1)
            primes = []
            isPrime[0] = False
            isPrime[1] = False

            for i in range(n):
                if isPrime[i]:
                    j = i
                    while i * j <= n:
                        isPrime[i*j] = False
                        j += 1

            for i in range(len(isPrime)):
                if isPrime[i]:
                    primes.append(i)

            return primes

        primes = sieve(n)

        def find_factor(n):
            factorSum = 0

            
            while n > 1:
                flag = False
                for prime in primes:
                    if n % prime == 0:
                        factorSum += prime
                        n //= prime 
                        flag = True
                        break
                if not flag:
                    return -1
            return factorSum 

        while True:
            n = find_factor(n)
            if n == -1 or n in seen:
                return mn

            seen.add(mn)
            mn = min(mn, n)
