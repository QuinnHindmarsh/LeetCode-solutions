def f(x):
    return (x * (x - 1)) >> 1

class Solution:
    def subsequencesWithMiddleMode(self, a: List[int]) -> int:
        n = len(a)
        ans = 0
        ml = {}  # count the number left to a[i]
        mr = {}
        for j in range(0, 1):
            if a[j] not in ml:
                ml[a[j]] = 0
            ml[a[j]] += 1
        for j in range(2, n):
            if a[j] not in mr:
                mr[a[j]] = 0
            mr[a[j]] += 1
        for i in range(2, n - 2):
            c = a[i]  # center
            
            cnt_l = 0
            for j in range(0, i):
                if c == a[j]:
                    cnt_l += 1
            cnt_r = 0
            for j in range(i + 1, n):
                if c == a[j]:
                    cnt_r += 1

            l0 = 0  # number of cases that l=0
            if i - cnt_l >= 2:
                l0 = f(i - cnt_l)
            r0 = 0
            if n - i - 1 - cnt_r >= 2:
                r0 = f(n - i - 1 - cnt_r)
            l1 = cnt_l * (i - cnt_l)  # number of cases that l=1
            r1 = cnt_r * (n - i - 1 - cnt_r)
            l2 = 0  # number of cases that l=2
            if cnt_l >= 2:
                l2 = f(cnt_l)
            r2 = 0
            if cnt_r >= 2:
                r2 = f(cnt_r)
            # l0 r2
            # l1 r1
            # l1 r2
            # l2 r0
            # l2 r1
            # l2 r2

            ans += l0 * r2
            ans += l1 * r1
            ans += l1 * r2
            ans += l2 * r0
            ans += l2 * r1
            ans += l2 * r2

            # l0 r1
            # l1 r0

            if a[i - 1] not in ml:
                ml[a[i - 1]] = 0
            ml[a[i - 1]] += 1
            mr[c] -= 1
            if mr[c] == 0:
                del mr[c]
            
            ll = 0  # #cases of selecting 2 same numbers at left
            for j in ml:
                if j != c and ml[j] >= 2:
                    ll += f(ml[j])
            rr = 0
            for j in mr:
                if j != c and mr[j] >= 2:
                    rr += f(mr[j])

            for j in ml:
                if j == c:
                    continue
                if j not in mr:
                    ans += cnt_l * (f(n - i - 1 - cnt_r) - rr) * ml[j]
                else:
                    ans += cnt_l * (f(n - i - 1 - cnt_r - mr[j]) - rr + f(mr[j])) * ml[j]
            for j in mr:
                if j == c:
                    continue
                if j not in ml:
                    ans += cnt_r * (f(i - cnt_l) - ll) * mr[j]
                else:
                    ans += cnt_r * (f(i - cnt_l - ml[j]) - ll + f(ml[j])) * mr[j]

            ans %= 1000000007
        return ans

            

            
            