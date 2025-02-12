class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_digits(num):
            ans = 0

            while num > 0:
                digit = num % 10
                num //= 10
                ans += digit
            
            return ans


        freqs = defaultdict(list)
        mx = -1

        for num in nums:
            digSum = sum_digits(num)
            freqs[digSum].append(num)

        for key in freqs:
            if len(freqs[key]) < 2:
                continue
            mx2 = -1
            mx1 = -1

            for val in freqs[key]:
                if val > mx1:
                    mx2 = mx1
                    mx1 = val
                elif val > mx2:
                    mx2 = val

            mx = max(mx, mx1 + mx2)
        
        return mx
