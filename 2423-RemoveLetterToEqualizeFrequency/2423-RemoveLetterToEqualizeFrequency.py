class Solution:
    def equalFrequency(self, word: str) -> bool:
        def nonZeroMin(arr):
            mn = float('inf')
            for val in arr:
                if val < mn and val > 0:
                    mn = val
            return mn

        def checkEven(arr):
            return nonZeroMin(arr) == max(arr)
        

        cnt = [0] * 26
        for c in word:
            cnt[ord(c)-ord('a')] +=1


        for i in range(26):
            if cnt[i] != 0:
                cnt[i] -=1
                if checkEven(cnt):
                    return True
                cnt[i] +=1
        
        return False

            