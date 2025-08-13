# Last updated: 13/08/2025, 11:32:50
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def sieve(n):
            nums = [True] * (n+1)
            nums[0] = False
            nums[1] = False

            for i in range(2,int(sqrt(n))+1):
                if nums[i] == False:
                    continue
                for j in range(i*i, n,i):
                    nums[j] = False
            return nums

        nums = sieve(n)
        primes = set()
        used = set()
        ans = []
        for i in range(len(nums)):
            if nums[i]:
                primes.add(i)

        for num in primes:
            complement = n - num
            if complement in primes and complement not in used:
                used.add(complement)
                used.add(num)
                ans.append((min(num, complement), max(num, complement)))

        ans.sort(key = lambda x: x[0])
        return ans

        
