class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = [0]

        # Creates a prefix sum array of the weights of a rectangle
        for rect in rects:
            # (hieght + 1) * (width + 1) + previous weight
            # We need to do + 1 to deal with the case of a  rectangle having either a hieght or width of 0
            self.weights.append((rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1) + self.weights[-1])


    def pick(self):
        # Picks a random rectangle taking weights into consideration
        randnum = randint(0,self.weights[-1])
        # Finds the rectangle picked
        for i in range(len(self.weights)):
            if self.weights[i] >= randnum:
                # Picks random points in that rectangle 
                u = randint(self.rects[i-1][0],self.rects[i-1][2])
                v = randint(self.rects[i-1][1],self.rects[i-1][3])
                return [u, v]
