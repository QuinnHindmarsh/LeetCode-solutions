class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.tar = target
        self.dp = {}
       
        return self.backtracking(0,0)

    def backtracking(self,curSum,i):
        if (curSum,i) in self.dp:
            return self.dp[(curSum,i)]

        if i == len(self.nums):
            
            return 1 if curSum == self.tar else 0
        self.dp[(curSum,i)] = self.backtracking(curSum+self.nums[i],i+1) +  self.backtracking(curSum-self.nums[i],i+1)
        return self.dp[(curSum,i)]