# Last updated: 30/06/2025, 18:49:38
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums2 = [-num for num in nums]
        heapify(nums2)

        for _ in range(k):
            num = heappop(nums2)

        return -num