class Solution {
    public int threeSumClosest(int[] nums, int target) {
        // sort arr
        // for for i position, do inward traversal with j and k 
        int l; int r; int csum = Integer.MAX_VALUE; int n = nums.length;
        Arrays.sort(nums);

        for (int i=0; i < n-2; i++){
            l = i+1; r = n -1;

            while (l < r){
                int sum = nums[i] + nums[l] + nums[r];
                if (Math.abs(target - sum) < Math.abs(target-csum)){
                    csum = sum;
                }

                if (sum > target){
                    r --;
                }else if (sum < target){
                    l++;
                }
                else{
                    break;
                }
            }
        }
        return csum;
    }
}