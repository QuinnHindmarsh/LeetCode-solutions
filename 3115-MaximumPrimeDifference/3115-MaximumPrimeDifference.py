class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def sieve(k):
            # 1-indexed
            primes = [True] * (k +1)
            primes[1] = False

            for i in range(2,k+1):
                if primes[i] == True:
                    for j in range(i+i,k+1,i):
    
                        primes[j] = False

            return primes
        primes = sieve(max(nums))
        l = r = None

        for i in range(len(nums)):
            if primes[nums[i]] == True:
                r = i
                if l == None:
                    l = i
        
        return r - l

        # O(n + max(n)log(log(max(n))))