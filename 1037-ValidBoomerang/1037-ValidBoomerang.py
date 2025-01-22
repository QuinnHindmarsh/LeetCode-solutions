class Solution:
    def isBoomerang(self, p: List[List[int]]) -> bool:
        a = p[1][1] # 2nd y
        b = p[0][1] # 1st y
        c = p[1][0] # 2nd x
        d = p[0][0] # 1st x
        e = p[2][1] # 3rd y
        g = p[2][0] # 3rd x

        p = (tuple(p[0]), tuple(p[1]), tuple(p[2]))
        if len(set(p)) != 3:
            return False

        print((a-b) * g-c )
        print((e-a) * c-d)
        if (a-b) * (g-c) == (e-a) * (c-d):
            return False
        return True

        # if (a-b) / (c-d) == (e-a) / (g-c):
        #     return False
        # return True