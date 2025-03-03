class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nset = set([i for i in range(1,k+1)])
        ans = 0

        for i in range(len(nums)-1, -1,-1):
            if not nset:
                return ans

            nset.discard(nums[i])
            ans +=1
        return ans