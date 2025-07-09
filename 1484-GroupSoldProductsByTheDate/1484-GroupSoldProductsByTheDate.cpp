// Last updated: 09/07/2025, 11:09:58
class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        int diff = 0;
        vector<int> diff_idx = {};

        for (int i = 0; i < s1.length(); i++){
            
            if (s1[i] != s2[i]){
                diff ++;
                diff_idx.push_back(i);
                if (diff > 2) {return false;}
            }

        }

        if (diff == 2){
            char a = s1[diff_idx[0]];
            char b = s1[diff_idx[1]];
            s1[diff_idx[0]] = b;
            s1[diff_idx[1]] = a;

            if (s1 == s2){
                return true;
            }

        }



        return diff == 0 ? true : false;
    }
};