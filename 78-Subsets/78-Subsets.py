# Last updated: 26/06/2025, 16:24:20
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        state = []

        def dfs(i):
            if i == len(nums):
                ans.append(state[:])
                return
            
            
            state.append(nums[i])
            dfs(i+1)
            state.pop()
            dfs(i+1)

        dfs(0)
        return ans
