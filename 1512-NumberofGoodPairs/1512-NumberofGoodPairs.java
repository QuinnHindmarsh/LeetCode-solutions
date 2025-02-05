class Solution {
    public int numIdenticalPairs(int[] nums) {
        int cnt = 0;
        int[] arr = new int[101];

        for (int i : nums){
            arr[i]++;
        }

        for(int i :arr){
            if (i != 0){
            cnt += i * (i-1) /2;
            }
        }
        return cnt;
    }
}