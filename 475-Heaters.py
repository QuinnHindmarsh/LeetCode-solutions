"""
475. Heaters
Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range. 

Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will the same.

"""

# Solution one O(m log m + n log n + max(m,n) log(max(abs(max(heaters) - min(houses)),abs(min(heaters) - max(houses)))))


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()

        # Checks if all houses can be heated with a given input
        def check(r):
            i = 0
            j = 0

            while i < len(houses):
                while abs(heaters[j] - houses[i]) > r:
                    j += 1
                    if j >= len(heaters):
                        return False
                i += 1
            return True

        # Decreases the search scope until the min value is found
        def bin_search():
            l, r = 0, max(abs(max(heaters) - min(houses)),
                          abs(min(heaters) - max(houses)))
            while l < r:
                mid = l + (r - l) // 2
                if check(mid):
                    r = mid
                else:
                    l = mid + 1
            return l

        return bin_search()

# Solution two - find max distance O(m + n)space O(m log m + n log n )


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Find closest and get closest where taken from https://www.geeksforgeeks.org/find-closest-number-array/
        def findClosest(arr, n, target):
            i = 0
            j = n
            mid = 0
            while (i < j):
                mid = (i + j) // 2

                if (arr[mid] == target):
                    return arr[mid]

                if (target < arr[mid]):

                    if (mid > 0 and target > arr[mid - 1]):
                        return getClosest(arr[mid - 1], arr[mid], target)

                    j = mid
                else:
                    if (mid < n - 1 and target < arr[mid + 1]):
                        return getClosest(arr[mid], arr[mid + 1], target)
                    i = mid + 1

            return arr[mid]

        def getClosest(val1, val2, target):

            if (target - val1 >= val2 - target):
                return val2
            else:
                return val1

        maxDist = 0
        houses.sort()
        heaters.sort()

        n = len(houses)
        m = len(heaters)

        for i in range(n):
            maxDist = max(maxDist, abs(
                houses[i] - findClosest(heaters, m, houses[i])))

        return maxDist


# My solution
# https://leetcode.com/problems/heaters/solutions/6212255/2-completely-different-binary-search-sol-8cm1/
