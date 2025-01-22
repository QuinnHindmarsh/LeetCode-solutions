class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        # Ascending order
        sat.sort()
        # Adds biggest element of satisfaction 
        ans = 0

        #no positive number is possible
        if sat[-1] <= 0:
            return 0
        
        # Itterates largest to smallest
        i = len(sat)-1
        # Used to decicde if worth including negative numbers
        psum = 0
        while i >= 0:
            if sat[i] < 0:
                if abs(sat[i]) > psum:
                    sat = sat[i+1:]
                    break

            psum += sat[i]
            i -=1

        # Multiplies it by its place (Dish's worth the least are cooked last)
        for i in range(len(sat)):
            ans += sat[i] * (i+1)

        return ans