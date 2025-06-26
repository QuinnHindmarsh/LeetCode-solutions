# Last updated: 26/06/2025, 16:23:02
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        state = []

        def dfs(i):
            ans.add(tuple(state))

            if i == len(nums):
                return
            
            
            state.append(nums[i])
            dfs(i+1)
            state.pop()
            dfs(i+1)

        dfs(0)
        return list(ans)
