# Last updated: 26/06/2025, 16:11:06
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)
        state = []

        def dfs():
            if len(state) == len(nums):
                ans.append(deepcopy(state))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                state.append(nums[i])
                dfs()
                state.pop()
                used[i] = False

        dfs()
        return ans
