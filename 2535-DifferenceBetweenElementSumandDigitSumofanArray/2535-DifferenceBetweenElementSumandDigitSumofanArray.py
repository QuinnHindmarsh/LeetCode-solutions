class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digitSum = 0
        elementSum = sum(nums)

        for num in nums:
            strNum = str(num)
            for i in range(len(strNum)):
                digitSum += int(strNum[i])

        return abs(elementSum - digitSum)