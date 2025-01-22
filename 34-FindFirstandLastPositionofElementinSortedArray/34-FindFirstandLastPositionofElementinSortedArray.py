class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(arr,tar,l,r):
            l, r = 0, len(arr) -1
            while l < r:
                mid = (l + r) // 2 
                if arr[mid] > tar:
                    r = mid -1
                elif arr[mid] < tar:
                    l = mid +1
                else:
                    r = mid

            return l if l < len(arr) and arr[l] == tar else -1

        
        def findRight(arr,tar,l,r):
            l, r = 0, len(arr) -1

            while l < r:
                mid = (l + r) // 2 + 1
                if arr[mid] > tar:
                    r = mid -1
                elif arr[mid] < tar:
                    l = mid +1
                else:
                    l = mid
            return r if r < len(arr) and arr[r] == tar else -1

        if len(nums) == 0:
            return [-1,-1]

        ans = [-1,-1]
        l = findLeft(nums,target,0,len(nums) -1)
        r = findRight(nums, target, 0, len(nums)-1)
        ans[0] = l 
        ans[1] = r 

        return ans

