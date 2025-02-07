class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        n = len(h)

        stack = []
        leftMost = [-1] * n 

        for i in range(n):
            while stack and h[stack[-1]] >= h[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]

            stack.append(i)
            
        stack = []
        rightMost = [n] * n 
        for i in range(n-1,-1,-1):
            while stack and h[stack[-1]] >= h[i]:
                stack.pop()
            
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)

        maxArea = 0

        for i in range(n):
            leftMost[i] += 1
            rightMost[i] -=1

            maxArea = max(maxArea, h[i] * (rightMost[i] - leftMost[i] +1))

        return maxArea