class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def compute_fib(k):
            fibNums = [1,1]

            while fibNums[-1] < k:
                fibNums.append(fibNums[-1] + fibNums[-2])

            return fibNums


        def min_fib_nums(k):
            fibNums = compute_fib(k)
            ans = 0

            for i in range(len(fibNums)-1,-1,-1):
                count = k // fibNums[i]
                ans += count
                k -= (fibNums[i] * count)

            return ans
        
        return min_fib_nums(k)

        
