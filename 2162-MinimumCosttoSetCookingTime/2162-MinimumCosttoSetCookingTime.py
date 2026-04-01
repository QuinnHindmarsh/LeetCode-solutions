# Last updated: 01/04/2026, 18:57:33
1class Solution:
2    def splitArray(self, nums: List[int]) -> int:
3        
4        def sieve(n): 
5            arr = [True]  * (n +2)
6            arr[0] = False
7            arr[1] = False
8
9            for i in range(n+2):
10                if arr[i]:
11                    for j in range(i**2,n+2,i): 
12                        arr[j] = False
13            return arr
14
15        primes = sieve(len(nums)) 
16        a = 0 
17        b = 0 
18
19        for i,num in enumerate(nums): 
20            if primes[i]:
21                a += num
22            else:
23                b += num
24
25        return abs(a-b)
26
27