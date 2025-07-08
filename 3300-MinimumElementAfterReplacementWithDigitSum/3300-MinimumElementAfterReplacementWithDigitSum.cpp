// Last updated: 08/07/2025, 16:36:22
class Solution {
public:
    int minElement(vector<int>& nums) {
        int mn = INT_MAX;

        for (int num: nums){
            mn = min(digitSum(num), mn);
        }
        return mn;

    }

    int digitSum(int n){
        int ans, digit;
        ans = 0;

        while (n > 0){
            digit = n % 10;
            n /= 10;

            ans += digit; 
        }

        return ans;

    }
};