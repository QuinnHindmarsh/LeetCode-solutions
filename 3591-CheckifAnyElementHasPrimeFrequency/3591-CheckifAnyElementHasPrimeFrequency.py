# Last updated: 10/03/2026, 13:33:17
1class Solution:
2    def checkPrimeFrequency(self, nums: List[int]) -> bool:
3        freq = Counter(nums)
4        
5        primes = [True] * (len(nums) +2)
6        primes[1] = False
7
8
9        def sieve():
10            for i in range(1,len(primes)):
11                if primes[i]:
12                    j = i
13                    while j + i < len(primes):
14                        j += i
15                        primes[j] = False
16
17        sieve()
18        for cnt in freq.values(): 
19            if primes[cnt]: 
20                return True
21
22        return False
23
24