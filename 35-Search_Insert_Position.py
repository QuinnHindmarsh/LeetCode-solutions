"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/description/

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


# Soltuion one - itterative O(log n) time and O(1) space
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                # Inclusive of this, as if mid is the next number up from target
                # This is where we would want to insert it
                right = mid
            elif nums[mid] < target:
                # We can exlcude mid from the search space as mid wont be either the value or the insertion index
                left = mid + 1
            else:
                return mid

        return right


# Solution two - recursive O(log n) time and space
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def bin_search(arr, left, right, tar):
            # Base case
            if not left < right:
                return left

            mid = left + (right - left) // 2

            if arr[mid] > tar:
                return bin_search(arr, left, mid, tar)
            elif arr[mid] < tar:
                return bin_search(arr, mid+1, right, tar)
            else:
                return mid

        return bin_search(nums, 0, len(nums), target)


# Solution three - bisect solution O(log n) time and O(1) space as bisect left is implemented itterativly
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)


# My solution
# https://leetcode.com/problems/search-insert-position/solutions/6195494/break-down-on-how-the-binary-search-work-4czc/
