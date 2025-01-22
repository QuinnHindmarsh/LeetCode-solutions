class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Makes all stones neggitive to turn the min heap into a max heap
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapify(stones)


        while stones:
            stone1 = heappop(stones)
            if stones:
                stone2 = heappop(stones)
            else:
                # Exactly one stone left, return the value of remaming stone
                return stone1 * -1
            
            #Makes sure no stones with weight of 0 are added
            #stone1 >= stone2. So the only condition we need to check is if they equal
            if stone1 != stone2:
                heappush(stones, stone1-stone2)
        # No stones left
        return 0
