class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        # for i in range(k):
        #     m = 0
        #     for j in range(len(nums)):
        #         if nums[j] < nums[m]:
        #             m = j
        #     nums[m] *= multiplier
        # return nums

        pq = [(x, i) for i, x in enumerate(nums)]
        heapify(pq)

        for _ in range(k):
            nums[pq[0][1]] = pq[0][0] * multiplier
            heapreplace(pq, (pq[0][0] * multiplier, pq[0][1]))

        return nums