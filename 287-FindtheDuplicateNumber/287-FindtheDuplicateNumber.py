class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Sets fast and slow to the inital state
        slow, fast = nums[0], nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # Increments slow and initalises slow2 
        slow = nums[slow]
        slow2 = nums[0]
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow
