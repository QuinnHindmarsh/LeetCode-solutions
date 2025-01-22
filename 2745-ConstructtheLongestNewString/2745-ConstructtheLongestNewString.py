class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # x - aa
        # y - bb
        # z - ab
        # no z after x
        # no x after x 
        # no y after z
        # no y after z

        # You can always use up all z as you can continously do zzz, so we add 2z to our final length
        # We can also repeat yz as many times as min(y,z)
        # If y != z we can increase this by 2 as an addional one of these can be added. e.g. either yxyz or xyzx
        if y == x:
            return (4 * x) + (2 * z) 
        else:
            return (4 * min(y,x)) + 2 + (2 * z) 

        
