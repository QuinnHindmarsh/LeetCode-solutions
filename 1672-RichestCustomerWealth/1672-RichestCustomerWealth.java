class Solution {
    public int maximumWealth(int[][] accounts) {
        int max = 0;
        for (int i = 0; i < accounts.length; i++){
            if (sumArr(accounts[i]) > max){
                max = sumArr(accounts[i]);
            }

        }
        return max;
    }

    public int sumArr(int[] arr){
        int ans = 0;

        for (int i=0; i < arr.length; i++){
            ans += arr[i];
        }

        return ans;
    }
}