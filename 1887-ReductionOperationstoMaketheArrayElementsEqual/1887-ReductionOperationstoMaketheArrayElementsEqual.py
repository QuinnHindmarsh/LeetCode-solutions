class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # Simulatrion would likely take to long - Use a max heap 
        # All elements will need to be reduced to the min, once it hits the min dont add it back
        # Can i maths this 
        mn = min(nums)
        n = len(nums)
        ans = 0
        freqs = []

        for i in range(n):
            nums[i] *= -1

        heapq.heapify(nums)

        while nums:
            val = heapq.heappop(nums)
            if val == -mn:
                break
            
            count = 1
            while nums and nums[0] == val:
                count +=1
                heapq.heappop(nums)
            freqs.append(count)
        
        m = len(freqs)
        for i in range(m):
            ans += freqs[i] * (m -i)
        
        return ans