public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        List<int> appearedNums = new List<int>();
        for (int i = 0; i < nums.Length; i++)
        {
            if (appearedNums.Contains(nums[i])) return true;
            else appearedNums.Add(nums[i]);
        }
        return false;
    }
}