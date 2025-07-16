// Last updated: 16/07/2025, 16:37:47
class Solution {
public:
    int hammingDistance(int x, int y) {
        bitset<32> bin_x (x);
        bitset<32> bin_y (y);
        int cnt = 0; 

        for (int i = 0; i < 32; i++){
            if (bin_x[i] != bin_y[i]){
                cnt++;
            } 
        }

        return cnt;
    }
};