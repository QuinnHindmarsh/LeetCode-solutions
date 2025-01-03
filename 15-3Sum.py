"""
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


"""

# Brute force O(n^3)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips = set()
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        trip = tuple(sorted([nums[i], nums[j], nums[k]]))
                        trips.add(trip)

        return list(trips)


# N^2
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        vals = {}
        trips = set()
        n = len(nums)

        # Adds all numbers and there index to a dict
        for i, num in enumerate(nums):
            if num in vals:
                vals[num].append(i)
            else:
                vals[num] = [i]

        # Optimisation, requried for AC
        if len(vals) == 1:
            for key in vals:
                if key * 3 == 0:
                    return [[vals[key][0], vals[key][0], vals[key][0]]]

        # For each pair sees if the complement is in the dict
        for i in range(n):
            for j in range(i+1, n):
                comp = -(nums[i] + nums[j])

                if comp in vals:
                    for idx in vals[comp]:
                        if idx != j and idx != i:
                            trip = tuple(sorted([nums[i], nums[j], nums[idx]]))
                            trips.add(trip)
                            break

        return list(trips)


# O(n^2) two pointer


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets = set()
        nums.sort()

        # for all value's of n we found all pairs in a single pass
        for i in range(n-2):
            v = nums[i]
            lp = i + 1
            rp = n - 1

            while lp < rp:
                if v + nums[lp] + nums[rp] == 0:
                    triplets.add((v, nums[lp], nums[rp]))
                    lp += 1
                    rp -= 1
                elif v + nums[lp] + nums[rp] > 0:
                    rp -= 1
                else:
                    lp += 1

        return list(triplets)

# my solution
# https://leetcode.com/problems/3sum/solutions/6220961/on2-two-pointer-on2-brute-force-by-quinn-vkej/
