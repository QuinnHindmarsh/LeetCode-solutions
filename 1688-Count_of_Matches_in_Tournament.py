"""
1688. Count of Matches in Tournament
You are given an integer n, the number of teams in a tournament that has strange rules:

If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
Return the number of matches played in the tournament until a winner is decided.

 
"""


# Solution one - ittertative simulation  O(log n) time and O(1) space
class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            # If even
            if n % 2 == 0:
                matches += n/2
                n = n / 2
            else:
                matches += (n-1)/2
                n = (n-1)/2 + 1
        return int(matches)

# Solution two - recursive simulation O(log n ) time and space


class Solution:
    def numberOfMatches(self, n: int, matches=0) -> int:
        if n == 1:
            return matches
        if n % 2 == 0:
            return self.numberOfMatches(n//2, matches + n // 2)
        else:
            return self.numberOfMatches(n//2 + 1, matches + n//2)


# Solution 3 maths- O(1) time and space
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1


# My solution
# https://leetcode.com/problems/count-of-matches-in-tournament/solutions/6211125/iterative-simulation-recursive-simulatio-3d13/
