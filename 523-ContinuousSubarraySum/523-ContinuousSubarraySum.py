class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {}
        prefixMod = 0

        for i,n in enumerate(nums):
            prefixMod = (prefixMod + n) % k
            if prefixMod == 0 and i >= 1: return True

            if prefixMod in seen:
                if i - seen[prefixMod] > 1:
                    return True
            else:
                seen[prefixMod] = i

        return False