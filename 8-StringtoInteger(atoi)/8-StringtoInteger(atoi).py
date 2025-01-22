class Solution:
    def myAtoi(self, s: str) -> int:
        snum = ""
        possitive = True
        flag = False

        i = 0
        while i < len(s):
            if s[i].isalpha():
                break
            if s[i] == " ":
                if len(snum) !=0:
                    break
            else:
                if s[i] == "-" and len(snum) ==0:
                    possitive = False
                    if flag:
                        break
                    flag = True
                elif s[i] == '+':
                    if flag or (i +1 < len(s) and not s[i+1].isnumeric()):
                        break
                    flag = True

                elif s[i] == "0" and len(snum) == 0:
                    if i +1 < len(s) and not s[i+1].isnumeric():
                        break
                elif not s[i].isnumeric():
                    break
                else:
                    snum += s[i]
            i +=1

        if snum == '':
            return 0
        num = int(snum)
        if not possitive:
            num = -abs(num)
        
        if num > (2**31) -1:
            return (2**31) -1
        elif num < -2**31:
            return -2**31
        return num