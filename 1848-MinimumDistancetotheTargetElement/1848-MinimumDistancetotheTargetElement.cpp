// Last updated: 08/07/2025, 16:44:35
class Solution {
public:
    int getMinDistance(vector<int>& nums, int target, int start) {
        int mn = INT_MAX;


        for (int i = 0; i < nums.size(); i++){
            if (nums[i] == target){
                mn = min(mn, abs(start - i));
            }
        }
        return mn;
    }
};