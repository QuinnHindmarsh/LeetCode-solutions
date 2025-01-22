class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        prefix = [nums[0]]
        n = len(nums)

        for i in range(1,len(nums)):
            prefix.append( nums[i] + prefix[i-1])

        for query in queries:
            cur = 0
            i = bisect_left(nums,query)
            if i > 0:
                cur += abs(prefix[i-1] - (query * i))
            if i < len(nums):
                rSum = prefix[-1] - prefix[i-1] if i > 0 else prefix[-1]
                cur += abs(rSum - (query*(n-i)))
            ans.append(cur)

        return ans