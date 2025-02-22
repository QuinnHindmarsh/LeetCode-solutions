    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack, res, n = [], [-1]*len(nums), len(nums)
        for i in xrange(0, 2*n):
            while stack and nums[i%n] > nums[stack[-1]]:
                top = stack.pop()
                if res[top] == -1:
                    res[top] = nums[i%n]
            stack.append(i%n)
        return res