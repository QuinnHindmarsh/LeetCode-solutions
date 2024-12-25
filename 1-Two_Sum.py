"""
1. Two Sum
https://leetcode.com/problems/two-sum/description/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""

# Solution one - O(n^2) time and O(1) space


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # Brute force tries all paris
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Solution two - O(n) time and O(n) space - two o(n) itterations
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}

        # Adds each value and the index to a hashmap
        for i in range(len(nums)):
            if nums[i] in vals:
                vals[nums[i]].append(i)
            else:
                vals[nums[i]] = [i]

        # For each number, checks if the complement exists
        for num in nums:
            if target - num == num:
                # Solutions need to be unique so the length will never be > 2 if target - num = num
                if len(vals[num]) == 2:
                    return vals[num]
            elif (target - num) in vals:
                return [vals[num][0], vals[target-num][0]]

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


# My solution
# https://leetcode.com/problems/two-sum/solutions/6183454/three-solutions-naive-hashmap-improved-h-rj3s/
