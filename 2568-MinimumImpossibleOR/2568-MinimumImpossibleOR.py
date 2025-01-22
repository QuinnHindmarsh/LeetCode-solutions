class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(33):
            if 1 << i not in nums:
                return 1 << i
        