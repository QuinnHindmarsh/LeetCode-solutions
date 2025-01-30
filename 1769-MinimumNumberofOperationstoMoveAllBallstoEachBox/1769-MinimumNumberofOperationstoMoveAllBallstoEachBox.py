class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        n = len(boxes)
        pleft = [0] * n 
        pright = [0] * n
        
        balls = 0
        for i in range(n):
            pleft[i] = pleft[i-1] + balls
            if boxes[i] == '1':
                balls += 1
        
        balls = 0 if boxes[-1] == '0' else 1
        for i in range(n-2,-1,-1):
            pright[i] = pright[i+1] + balls
            if boxes[i] == '1':
                balls += 1

        for i in range(n):
            ans.append(pleft[i] + pright[i])


        return ans