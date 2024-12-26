"""
198. House Robber
https://leetcode.com/problems/house-robber/description/
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""

# Solution 1 - O(n) time and space


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Dealing with edge case - if there is only one house, robbing that is the optimal solution
        if n == 1:
            return nums[0]

        # Sets the first two items in the dp array as being the first 2 houses.
        # As that is the max you can rob at that point
        dp_array = [0] * len(nums)
        dp_array[0], dp_array[1] = nums[0], nums[1]

        for i in range(2, n):
            v1 = dp_array[i-2]
            v2 = 0

            if i - 3 >= 0:
                v2 = dp_array[i-3]

            # Finds the max possible value you can rob up to this house, while still robbing this house
            dp_array[i] = max(v1, v2) + nums[i]

        # The optimal solution will always rob either the last or second last house
        return max(dp_array[-1], dp_array[-2])

# Solution two - O(N) time and O(1) spacew


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = maxRob = 0

        # For each house it sees if you are best off robbing i-2 + the current one, or i-1
        for house in nums:
            temp = maxRob
            maxRob = max(maxRob, prev + house)
            prev = temp

        return maxRob

# My solutions
# https://leetcode.com/problems/house-robber/solutions/6187184/on-space-and-o1-space-by-quinnhindmarsh-w91f/
