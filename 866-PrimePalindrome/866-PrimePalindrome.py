# Last updated: 11/08/2025, 17:46:02
class Solution:
    def largestPalindromic(self, num: str) -> str:
        nums = defaultdict(int)
        ans = []
        max_rem = '-1'
        for i in range(len(num)):
            nums[num[i]] += 1

        keys= sorted(nums.keys(), reverse=True)

        for key in keys:
            if key == "0":
                if nums[key] %2 == 1 and max_rem == '-1':
                    max_rem = '0'
                continue

            while nums[key] >= 2:
                nums[key] -= 2
                ans.append(key)
            if nums[key] == 1 and max_rem == '-1':
                max_rem = key

        if len(ans) == 0:
            return max_rem if max_rem != '-1' else '0'


        if max_rem != '-1':
            return ''.join(ans) + ('0' * (nums['0']//2)) + max_rem  + ('0' * (nums['0']//2)) + ''.join(ans[::-1])

        return ''.join(ans) + ('0' * (nums['0'])) + ''.join(ans[::-1])