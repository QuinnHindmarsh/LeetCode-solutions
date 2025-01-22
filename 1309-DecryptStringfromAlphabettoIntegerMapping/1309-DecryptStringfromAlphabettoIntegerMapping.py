class Solution(object):
    def freqAlphabets(self, s):

        txt = ''
        i = 0
        while i < (len(s)):
            if i+2 < len(s) and s[i+2] == '#':
                num = s[i] + s[i+1]
                i += 3
            else:
                num = s[i]
                i += 1
        
            txt += chr(int(num)+96)
        return txt