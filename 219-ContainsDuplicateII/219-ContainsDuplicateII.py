class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        locs = {}

        for i in range(len(nums)):
            if nums[i] in locs:
                locs[nums[i]].append(i)
            else:
                locs[nums[i]] = [i]
        
        for key in locs:
            for i in range(len(locs[key])):
                for j in range(i+1,len(locs[key])):
                    if abs(locs[key][i] - locs[key][j]) <= k:
                        return True
        return False