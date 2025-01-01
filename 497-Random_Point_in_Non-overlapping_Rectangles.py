"""
497. Random Point in Non-overlapping Rectangles

You are given an array of non-overlapping axis-aligned rectangles rects where rects[i] = [ai, bi, xi, yi] indicates that (ai, bi) is the bottom-left corner point of the ith rectangle and (xi, yi) is the top-right corner point of the ith rectangle. Design an algorithm to pick a random integer point inside the space covered by one of the given rectangles. A point on the perimeter of a rectangle is included in the space covered by the rectangle.

Any integer point inside the space covered by one of the given rectangles should be equally likely to be returned.

Note that an integer point is a point that has integer coordinates.

Implement the Solution class:

Solution(int[][] rects) Initializes the object with the given rectangles rects.
int[] pick() Returns a random integer point [u, v] inside the space covered by one of the given rectangles.

"""


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = [0]

        # Creates a prefix sum array of the weights of a rectangle
        for rect in rects:
            # (hieght + 1) * (width + 1) + previous weight
            # We need to do + 1 to deal with the case of a  rectangle having either a hieght or width of 0
            self.weights.append(
                (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1) + self.weights[-1])

    def pick(self):
        # Picks a random rectangle taking weights into consideration
        randnum = randint(0, self.weights[-1])
        # Finds the rectangle picked
        for i in range(len(self.weights)):
            if self.weights[i] >= randnum:
                # Picks random points in that rectangle
                u = randint(self.rects[i-1][0], self.rects[i-1][2])
                v = randint(self.rects[i-1][1], self.rects[i-1][3])
                return [u, v]

# My solution
# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/solutions/6210960/prefix-sum-solution-in-depth-explanation-m7dl/
