
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