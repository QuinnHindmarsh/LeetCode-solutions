class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    
        def bin_search(arr,left,right,tar):
            # Base case
            if left >= right: return left

            mid = left + (right - left) //2

            if arr[mid] > tar:
                return bin_search(arr,left,mid,tar)
            elif arr[mid] < tar:
                return bin_search(arr,mid+1,right,tar)
            else:
                return mid
            

        
        return bin_search(nums,0,len(nums),target)