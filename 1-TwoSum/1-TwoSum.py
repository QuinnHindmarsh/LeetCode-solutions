# Solution three - O(n) time and o(n) space - one O(n) itteration
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}

        # For each number, it checks if the complment is in the hashmap already - if not it adds it
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in vals:
                return [i, vals[complement]]

            vals[nums[i]] = i