class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a,b = b,a

        flag = False
        ans = ""
        i = 0

        while i < len(a):
            numOnes = int(flag) + int(a[(-1-i)])
            if i < len(b):
                numOnes += int(b[(-1-i)])
            flag = False

            if numOnes % 2 == 1:
                ans += '1'
                numOnes -= 1
            else:
                ans += '0'
            
            if numOnes == 2:
                flag = True
            
            i += 1
        
        if flag:
            ans += '1'
        

        return ans[::-1]