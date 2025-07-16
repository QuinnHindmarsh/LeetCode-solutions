// Last updated: 16/07/2025, 13:05:11
class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        map<int, int> freqs;
        int mx_cnt = 0;
        int mx_sum = 0;

        for (int i = 0; i < nums.size(); i++){
            int n = nums[i];
            
            if (freqs.find(n) == freqs.end()){
                freqs[n] = 0;
            }
            freqs[n]++;
        } 

        for (auto itr = freqs.begin(); itr != freqs.end(); itr++ ){
            int cnt = itr->second;
            if (cnt > mx_cnt){
                mx_cnt = cnt; 
                mx_sum = 0;
            }
            if (cnt == mx_cnt){
                mx_sum += cnt; 
            }
        }
        return mx_sum;
    }
};