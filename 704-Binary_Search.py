"""
704. Binary Search
https://leetcode.com/problems/binary-search/description/
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

# Solution one - recurisve O(log n) time O(log n) space


class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        def bin_search(high, low, tar):
            # Include last element in search space
            if low <= high:
                # Use mid = low + (high - low) // 2 in other languages
                # To prevent int overflow
                mid = (high + low) // 2

                if nums[mid] > tar:
                    # Dont include mid in serch space
                    return bin_search(mid-1, low, tar)
                if nums[mid] < tar:
                    # Dont include mid in serch space
                    return bin_search(high, mid+1, tar)
                else:
                    return mid
            else:
                return -1

        return bin_search(len(nums)-1, 0, tar)


# Solution two - itterative O(log n) time and O(1) space
class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        low = 0
        high = len(nums) - 1
        # Inclusive of last element in search space
        while low <= high:
            mid = low + (high - low) // 2
            if tar > nums[mid]:
                # Exlcudes mid from search space
                low = mid + 1
            elif tar < nums[mid]:
                # Exlcudes mid from search space
                high = mid - 1
            else:
                return mid
        return -1


# Solution three - cheating, recurisve O(log n) time O(log n) space
class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        i = bisect_left(nums, tar)

        # insertion point points to the number itself
        # and the insertion point isnt the end of the list
        if i != len(nums) and nums[i] == tar:
            return i
        else:
            return -1

# My solution
# https://leetcode.com/problems/binary-search/solutions/6190926/recursive-iterative-bisect-solution/
