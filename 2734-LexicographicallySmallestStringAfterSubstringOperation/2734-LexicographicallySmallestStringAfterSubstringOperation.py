class Solution:
    def smallestString(self, s: str) -> str:
        lp = rp = 0
        new_s = ''
        # Deal with non-empty subset

        if s == 'a' * len(s):
            return 'a' *(len(s) -1) + 'z'

        for i in range(len(s)):
            if s[i] != 'a':
                lp = i
                break

        for i in range(lp,len(s)):
            if s[i] == 'a':
                rp = i -1
                break
            elif i == len(s) -1:
                rp = i 
                break
        


        for i in range(len(s)):
            if i <= rp and i >= lp:
                new_s += chr(ord(s[i]) -1)
            else:
                new_s += s[i]
        
        return new_s