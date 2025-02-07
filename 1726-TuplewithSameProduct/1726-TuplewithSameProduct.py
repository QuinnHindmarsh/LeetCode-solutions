class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freqs = defaultdict(int)
        ans = 0

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                freqs[nums[i]*nums[j]] += 1

        
        for key in freqs:
            cnt = freqs[key]
            if cnt > 1:
                cnt *= 2 
                ans += (cnt**2) - (cnt * 2)  
        
        return ans