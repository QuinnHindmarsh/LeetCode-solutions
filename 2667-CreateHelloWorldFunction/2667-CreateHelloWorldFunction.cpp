// Last updated: 14/07/2025, 12:29:12
class Solution {
public:
    bool canBeIncreasing(vector<int>& nums) {

        for (int i = 0; i < nums.size(); i++){
            bool valid = true;
            for (int j = 1; j < i; j++){
                if (nums[j] <= nums[j-1]){
                    valid = false;
                }
            }

            if (i != 0 && i +1 < nums.size() && nums[i+1] <= nums[i-1]){
                valid = false;
            }

            for (int j = i+2; j < nums.size(); j++){
                if (nums[j] <= nums[j-1]){
                    valid = false;
                }
            }

            if (valid){
                return true;
            }
        }

        return false;
    }
};