class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s) +1)
        alph = [chr(97 + i) for i in range(26)]
        
        for sh in shifts:
            if sh[2] == 1:
                arr[sh[0]] += 1
                arr[sh[1] +1] -= 1
            else:
                arr[sh[0]] -= 1
                arr[sh[1] +1] += 1

        csum = 0
        s = list(s)
        for i in range(len(s)):
            csum += arr[i]  
            new_index = (ord(s[i]) - 97 + csum) % 26  
            s[i] = chr(97 + new_index) 

        return "".join(s)