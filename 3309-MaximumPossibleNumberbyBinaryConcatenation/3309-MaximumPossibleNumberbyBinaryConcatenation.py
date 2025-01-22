class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        return max(int(''.join(x),base=2) for x in permutations(bin(b)[2:] for b in nums))