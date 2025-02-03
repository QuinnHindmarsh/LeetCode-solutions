class Solution:
    def threeSumClosest(self, nums: List[int], tar: int) -> int:
        # right biased
        def bin_search(l, arr, tar):
            r = len(arr) - 1
            while l < r:
                mid = l + (r-l) // 2
                if arr[mid] > tar:
                    r = mid
                elif arr[mid] < tar:
                    l = mid + 1 
                else:
                    return mid 
            return r

        nums.sort()
        n = len(nums)
        closetSum = float('inf')
        for i in range(n-2):
            for j in range(i+1, n-1):
                complement = tar - (nums[i] + nums[j])
                idx = bin_search(j+1, nums, complement)
                total1 = nums[idx] + nums[i] + nums[j] # 10
                total2 = nums[idx-1] + nums[i] + nums[j] if idx > 0 and idx > (j + 1) else float('inf')
                if abs(tar - total1) < abs(tar - total2):
                    closet = total1
                else:
                    closet = total2
                if abs(tar - closetSum) > abs(tar - closet):
                    closetSum = closet
        return closetSum
