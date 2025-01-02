"""
1402. Reducing Dishes
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

Return the maximum sum of like-time coefficient that the chef can obtain after preparing some amount of dishes.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
"""


class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        # Ascending order
        sat.sort()
        # Adds biggest element of satisfaction
        ans = 0

        # no positive number is possible
        if sat[-1] <= 0:
            return 0

        # Itterates largest to smallest
        i = len(sat)-1
        # Used to decicde if worth including negative numbers
        psum = 0
        while i >= 0:
            if sat[i] < 0:
                if abs(sat[i]) > psum:
                    sat = sat[i+1:]
                    break

            psum += sat[i]
            i -= 1

        # Multiplies it by its place (Dish's worth the least are cooked last)
        for i in range(len(sat)):
            ans += sat[i] * (i+1)

        return ans

# My solution
# https://leetcode.com/problems/reducing-dishes/solutions/6215729/intuitive-solution-with-explanation-by-q-plsr/
