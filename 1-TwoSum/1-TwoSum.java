class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> vals = new HashMap<>();
        ArrayList<Integer> ans = new ArrayList<>();
        
        for (int i = 0; i < nums.length; i ++){
            int complement = target - nums[i];

            System.out.println(complement);

            if(vals.containsKey(complement)){
                return new int[] {i, vals.get(complement)};
            }
            vals.put(nums[i], i);
        }
        return new int[] {};

    }
}