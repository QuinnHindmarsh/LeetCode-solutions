class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0

        for num in nums:
            n = num
            cur = 0
            if n - 1 not in nums:
                while n + 1 in nums:
                    n += 1
                    cur += 1

        
            ans = max(ans,cur+1) 
        return ans