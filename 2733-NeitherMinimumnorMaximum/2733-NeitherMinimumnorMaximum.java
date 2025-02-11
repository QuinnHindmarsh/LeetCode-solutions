class Solution {
    public int findNonMinOrMax(int[] nums) {
        // int mx = Collections.max(nums);
        // int mn = Collections.min(nums);
        int mx = Collections.max(Arrays.asList(Arrays.stream(nums).boxed().toArray(Integer[]::new)));
        int mn = Collections.min(Arrays.asList(Arrays.stream(nums).boxed().toArray(Integer[]::new)));
        

        for (int i: nums){
            if (i != mx && i != mn){
                return i;
            }
        }
        return -1;
    }
}