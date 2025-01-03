"""
2442. Count Number of Distinct Integers After Reverse Operations

You are given an array nums consisting of positive integers.

You have to take each integer in the array, reverse its digits, and add it to the end of the array. You should apply this operation to the original integers in nums.

Return the number of distinct integers in the final array.

 
"""

# Sol 1


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seen = set()
        ans = 0

        for num in nums:
            r = int(str(num)[::-1])
            if r not in seen:
                seen.add(r)
                ans += 1

            if num not in seen:
                seen.add(num)
                ans += 1

        return ans

# Sol 2


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        return len(set(nums + [int(str(num)[::-1]) for num in nums]))

# My solution
# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/solutions/6216918/simple-one-line-by-quinnhindmarsh-4t5h/
