// Last updated: 23/03/2026, 20:42:37
1class Solution {
2public:
3    bool canPartition(vector<int>& nums) {
4        int total = accumulate(nums.begin(), nums.end(), 0);
5        if (total % 2 == 1) return false;
6
7        int target = total / 2;
8        int n = nums.size();
9        vector<vector<int>> memo(n, vector<int>(target + 1, -1));
10
11        function<bool(int, int)> dp = [&](int i, int sm) -> bool {
12            if (sm == target) return true;
13            if (i >= n || sm > target) return false;
14            if (memo[i][sm] != -1) return memo[i][sm];
15
16            memo[i][sm] = dp(i + 1, sm) || dp(i + 1, sm + nums[i]);
17            return memo[i][sm];
18        };
19
20        return dp(0, 0);
21    }
22};