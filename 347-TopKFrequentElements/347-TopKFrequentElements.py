class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        buckets = [[] for i in range(len(nums) +1)]
        topK = []
        for num in nums:
            freq[num] +=1
        
        for num, cnt in freq.items():
            buckets[cnt].append(num)

        for i in range(len(buckets) -1 ,-1,-1):
            for num in buckets[i]:
                topK.append(num)

                if len(topK) == k:
                    return topK
