class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        currentConsec = 1
        maxConsec = 1
        nums.sort()

        if len(nums) == 0:
            return 0
        print(nums)
        for i in range(1,len(nums),1):
            if nums[i] == nums[i-1] + 1:
                currentConsec += 1
            elif nums[i] == nums[i-1]:
                pass
            else:
                if currentConsec > maxConsec:
                    maxConsec = currentConsec
                currentConsec = 1
        
        if currentConsec > maxConsec:
            return currentConsec
        return maxConsec