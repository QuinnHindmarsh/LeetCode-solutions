class Solution:
    def clearDigits(self, s: str) -> str:
        s_list = list(s)
        ans = ''
        cnt = 0

        while s_list:
            char = s_list.pop()

            if not char.isalpha():
                cnt += 1
            elif cnt >= 1:
                cnt -= 1
            else:
                ans += char

        return ''.join(ans[::-1])