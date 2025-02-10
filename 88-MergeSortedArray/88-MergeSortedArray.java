class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int l1 = 0; int l2 = 0;
        int i = 0;
        int[] arr = new int[(m + n)];

        while (l1 < m && l2 < n){
            if (nums1[l1] < nums2[l2]){
                arr[i] = nums1[l1];
                l1 ++;
            }else{
                arr[i] = nums2[l2];
                l2 ++;
            }
            i ++;
        }

        while (l1 < m){
            arr[i] = nums1[l1];
            l1 ++;
            i ++;
        }

        while (l2 < n){
            arr[i] = nums2[l2];
            l2++;
            i ++;
        }

        for (i = 0; i < (m + n); i++){
            nums1[i] = arr[i];
        }
    }
}