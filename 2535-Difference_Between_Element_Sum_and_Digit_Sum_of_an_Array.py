"""
2535. Difference Between Element Sum and Digit Sum of an Array
You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.
"""

# Solutuion one - readible O(m) time where m is the amount of digits and O(1) space


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digitSum = 0
        elementSum = sum(nums)

        for num in nums:
            strNum = str(num)
            for i in range(len(strNum)):
                digitSum += int(strNum[i])

        return abs(elementSum - digitSum)

# Solution two - one line, O(m) time and space


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(list((int(digit) for num in nums for digit in str(num)))) - sum(nums))


# My solution
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/solutions/6212002/one-line-solution-by-quinnhindmarsh-nn3a/
